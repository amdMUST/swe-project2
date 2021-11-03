import flask, json, os
from dotenv import load_dotenv, find_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_manager, login_required, current_user, login_user
from flask_login.utils import logout_user

from py_files.nyt import *
from py_files.tripmap import *
from py_files.weather import *

app = flask.Flask(__name__, static_folder='./build/static')

# get the Database URL and change it to postgresql if needed
load_dotenv(find_dotenv())
uri = os.environ.get('DATABASE_URL')
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)

# app configs
app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.urandom(16)

# create the database and get the classes from models.py
db = SQLAlchemy(app)
from py_files.models import *
db.create_all()

# initialize items needed for flask-login
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

bp = flask.Blueprint("bp", __name__, template_folder="./build")

@bp.route('/index')
#@login_required Uncomment when login is working
def index():
    # TODO: insert the data fetched by your app main page here as a JSON
    DATA = {"your": "data here"}
    data = json.dumps(DATA)
    return flask.render_template(
        "index.html",
        data=data,
    )

app.register_blueprint(bp)

# Login Manager handlers
@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return UserDB.query.get(int(user_id))

@app.teardown_appcontext
def shutdown_session(exception=None):
    db.session.remove()

# signup pages
@app.route('/signup')
def signup():
    return flask.render_template('signup.html')

@app.route('/signup', methods=["POST"])
def signup_post():
	...

# login pages
@app.route('/login')
def login():
    return flask.render_template('login.html')

@app.route("/logout")
@login_required
def logout():
    
    # logout the current user with flask login and redirect to main page
    user = current_user
    user.authenticated = False
    logout_user()
    return flask.redirect(flask.url_for('/'))

@app.route('/login', methods=["POST"])
def login_post():
	...

@app.route('/save', methods=["POST"])
def save():
    ...

@app.route('/')
def main():
	# will redirect the user to the appropriate page according to if they are logged in
    if current_user.is_authenticated:
        return flask.redirect(flask.url_for('bp.index'))
    return flask.redirect(flask.url_for('login'))


if __name__ == "__main__":
    app.run(
        debug=True, 
        host="0.0.0.0", 
        port=int(os.getenv("PORT", 8080))
        )
