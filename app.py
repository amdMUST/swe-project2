import requests, os, json, flask
from dotenv import load_dotenv, find_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_login import (
    LoginManager,
    login_manager,
    login_required,
    current_user,
    login_user,
)
from flask_login.utils import logout_user
from oauthlib.oauth2 import WebApplicationClient
from psycopg2.errors import UniqueViolation

from py_files.nyt import *
from py_files.tripmap import *
from py_files.weather import *
from py_files.city import *
from py_files.cityimg import *

app = flask.Flask(__name__, static_folder="./build/static")

# get the Database URL and change it to postgresql if needed
load_dotenv(find_dotenv())
uri = os.environ.get("DATABASE_URL")
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)

# app configs
app.config["SQLALCHEMY_DATABASE_URI"] = uri
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = os.urandom(16)

# Google configs
GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET")
GOOGLE_DISCOVERY_URL = "https://accounts.google.com/.well-known/openid-configuration"

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

# OAuth 2 client setup
client = WebApplicationClient(GOOGLE_CLIENT_ID)

# create the database and get the classes from models.py
db = SQLAlchemy(app)
from py_files.models import *

db.create_all()

# initialize items needed for flask-login
login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)

# construct api classes
n_client = nyt_client()
w_client = weather_client()
c_manager = city_manager()
OpenMap = OpenTripMap()
i_client = cityimg_client()

bp = flask.Blueprint("bp", __name__, template_folder="./build")

# Login Manager handlers
@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return UserDB.query.get(int(user_id))


@app.teardown_appcontext
def shutdown_session(exception=None):
    db.session.remove()


def get_google_provider_cfg():
    return requests.get(GOOGLE_DISCOVERY_URL).json()


@app.route("/")
def main():
    # will redirect the user to the appropriate page according to if they are logged in
    if current_user.is_authenticated:
        return flask.redirect(flask.url_for("bp.index"))
    return flask.redirect(flask.url_for("login"))


@bp.route("/index")
@login_required
def index():

    DATA = {
        "city_list": c_manager.get_city_list(),
        "user_id": current_user.user_id,
        "user_email": current_user.email,
        "user_name": current_user.name,
        "user_pic": current_user.pic,
    }
    data = json.dumps(DATA)
    return flask.render_template(
        "index.html",
        data=data,
    )


# react fetch requests
# saves city to users db and sends back an OK response if nothing goes wrong
@app.route("/save_city", methods=["POST"])
@login_required
def save_city():

    # need to fill out
    city = flask.request.json.get("city")
    db_city_check = CityDB.query.filter_by(city_name=city).all()
    db_user_check = CityDB.query.filter_by(user_id=current_user.user_id).all()
    if not db_city_check and db_user_check:
        liked_city = CityDB(user_id=current_user.user_id, city_name=city)
        db.session.add(liked_city)
        db.session.commit()
        print(True)
        return flask.jsonify({"Saved_City": "yes"})

    # send information back to the react frontend page
    return flask.jsonify({"Saved_City": "No, city has already been saved"})


# gets info about the requested city and sends back the info
@app.route("/get_city", methods=["POST"])
@login_required
def get_city():

    # retrieve name of city that we need to render
    city = flask.request.json.get("city")

    # get all the information for that specific city
    i_client.get_cityimg_url(city)
    w_client.getWeather(city)
    n_client.get_article_data(city)
    OpenMap.getInfo(city)
    opentrip = OpenMap.names
    opentripimages = OpenMap.img

    DATA = {
        "city": city,
        "city_image": i_client.getCityImg(),
        "weather_info": w_client.getMap(),
        "article_info": n_client.getArticle(),
        "opentrip": list(opentrip[0:3]),
        "opentripimages": list(opentripimages[0:3]),
    }

    # send information back to the react frontend page
    return flask.jsonify(DATA)


app.register_blueprint(bp)

# login pages
@app.route("/login")
def login():
    return flask.render_template("login.html")


@app.route("/login_post")
def login_post():
    google_provider_cfg = get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]

    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=flask.request.base_url + "/google-auth",
        scope=["openid", "email", "profile"],
    )
    return flask.redirect(request_uri)


@app.route("/login_post/google-auth")
def google_auth():
    # Get authorization code Google sent back to you
    code = flask.request.args.get("code")

    google_provider_cfg = get_google_provider_cfg()
    token_endpoint = google_provider_cfg["token_endpoint"]

    # Prepare and send a request to get tokens! Yay tokens!
    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_response=flask.request.url,
        redirect_url=flask.request.base_url,
        code=code,
    )
    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET),
    )

    # Parse the tokens!
    client.parse_request_body_response(json.dumps(token_response.json()))

    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)

    if userinfo_response.json().get("email_verified"):
        unique_id = userinfo_response.json()["sub"]
        users_email = userinfo_response.json()["email"]
        picture = userinfo_response.json()["picture"]
        users_name = userinfo_response.json()["given_name"]
    else:
        return "User email not available or not verified by Google.", 400

    # check if user is in db
    newUser = UserDB(user_id=unique_id, email=users_email, name=users_name, pic=picture)
    if isUserInDB(unique_id) == False:
        # if not add them to db
        db.session.add(newUser)
        db.session.commit()

    # Begin user session by logging the user in
    login_user(newUser, remember=True)
    newUser.authenticated = True

    # Send user back to homepage
    return flask.redirect(flask.url_for("main"))


@app.route("/logout")
@login_required
def logout():

    # logout the current user with flask login and redirect to main page
    user = current_user
    user.authenticated = False
    logout_user()
    return flask.redirect(flask.url_for("main"))


cityList = []
listLength = len(cityList)


@app.route("/profile", methods=["POST", "GET"])
@login_required
def profile():
    global cityList
    global listLength

    cityListDB = CityDB.query.filter_by(user_id=current_user.user_id).all()
    cityList.clear()
    for city in cityListDB:
        try:
            cityList.extend([city.city_name])
        except IndexError:
            pass
    listLength = len(cityList)

    return flask.render_template(
        "profile.html",
        user_name=current_user.name,
        user_id=current_user.user_id,
        user_pic=current_user.pic,
        cityList=cityList,
        listLength=listLength,
    )


@app.route("/Static_City", methods=["POST", "GET"])
@login_required
def Static_City():
    city = flask.request.form["cityPost"]
    i_client.get_cityimg_url(city)
    w_client.getWeather(city)
    n_client.get_article_data(city)
    OpenMap.getInfo(city)
    opentrip = OpenMap.names
    opentripimages = OpenMap.img
    city_imageinfo = i_client.getCityImg()
    weather_info = w_client.getMap()
    article_info = n_client.getArticle()
    city_image = city_imageinfo[0][1]
    article_info_headlines = article_info[0][1]
    article_info_abstract = article_info[1][1]
    article_info_img_url = article_info[2][1]
    weather_main = weather_info[0][1]
    weather_desc = weather_info[1][1]
    temp = weather_info[2][1]
    feels_like = [3][0]
    temp_min = [4][0]
    temp_max = [5][0]
    pressure = weather_info[6][1]
    humidity = weather_info[7][1]
    clouds = weather_info[8][1]
    wind = weather_info[9][1]
    user_id = current_user.user_id
    user_email = current_user.email
    user_name = current_user.name
    user_pic = current_user.pic

    print(city_image)
    return flask.render_template(
        "Static_City.html",
        opentrip=opentrip,
        opentripimages=opentripimages,
        city=city,
        city_image=city_image,
        weather_info=weather_info,
        article_info_headlines=article_info_headlines,
        article_info_abstract=article_info_abstract,
        article_info_img_url=article_info_img_url,
        weather_main=weather_main,
        weather_desc=weather_desc,
        temp=temp,
        feels_like=feels_like,
        temp_min=temp_min,
        temp_max=temp_max,
        pressure=pressure,
        humidity=humidity,
        clouds=clouds,
        wind=wind,
        user_id=user_id,
        user_email=user_email,
        user_name=user_name,
        user_pic=user_pic,
    )


# Function for checking if a user is already in the database already
def isUserInDB(userID):

    result = UserDB.query.filter_by(user_id=userID).all()

    # if we get a non-empty result from the DB, that means they already exist
    if result:
        return True

    return False


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.getenv("PORT", 8080)))
