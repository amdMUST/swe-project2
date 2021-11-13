import requests, flask, json, os
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

from py_files.nyt import *
from py_files.tripmap import OpenTrip, OpenTripImages
from py_files.weather import *

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

# does this work on heroku ?
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
w_client = weather_client()

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

    city = "Atlanta"  # Replace this with a function that retrieves the first index of a shuffled list of city names
    w_client.get_weather(city)
    opentrip = OpenTrip(city)
    opentripimages = OpenTripImages(city)
    DATA = {
        "city": city,
        "weather_info": w_client.getMap(),
        "opentrip": opentrip,
        "opentripimages": opentripimages,
        "user_id": current_user.user_id,
        "user_email": current_user.email,
        "user_name": current_user.name,
    }
    data = json.dumps(DATA)
    return flask.render_template(
        "index.html",
        data=data,
    )


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
    result = UserDB.query.filter_by(user_id=unique_id).all()
    newUser = UserDB(user_id=unique_id, email=users_email, name=users_name)

    if not result:
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


@app.route("/save", methods=["POST"])
def save():
    ...


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=int(os.getenv("PORT", 8080)))
