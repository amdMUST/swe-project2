from flask_login import UserMixin
from app import db

# FEEL FREE TO EDIT THESE TABLES, CURRENTLY JUST FILLER FROM PROJECT 1. TABLE 1 SHOULD BE GOOD FOR OUR
# USER TABLE THO, AND SECOND TABLE SHOULD BE THE ONE WHERE WE KEEP TRACK OF WHAT CITY THE USER ADDED

# UniqueID and Username db
class UserDB(UserMixin, db.Model):
    __tablename__ = "UserDB"
    user_id = db.Column(db.Float, unique=True, primary_key=True)
    email = db.Column(db.String(80), unique=True)
    name = db.Column(db.String(80), unique=True)
    pic = db.Column(db.String(120), unique=True)

    def __repr__(self):
        return "<User_id = %s, Email = %s, Name = %s, Pic = %s>" % (
            self.user_id,
            self.email,
            self.name,
            self.pic,
        )

    def get_id(self):
        """Return the id from the username."""
        return self.user_id

    def is_active(self):
        """True, as all users are active."""
        return True


class CityDB(UserMixin, db.Model):
    __tablename__ = "CityDB"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Float)
    city_name = db.Column(db.String(80))
