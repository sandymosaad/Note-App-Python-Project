# Import the database instance from the __init__.py file
from . import db

# Import UserMixin from Flask-Login for user authentication features
from flask_login import UserMixin

# Import func from SQLAlchemy to use database functions like "now()"
from sqlalchemy.sql import func


# Define the Note table (model)
class Note(db.Model):
    # Primary key (unique ID for each note)
    id = db.Column(db.Integer, primary_key=True)

    # The content/text of the note
    data = db.Column(db.String(10000))

    # The date/time when the note was created (default = current time)
    date = db.Column(db.DateTime(timezone=True), default=func.now())

    # Foreign key linking the note to the user who created it
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))



# Define the User table (model)
class User(db.Model, UserMixin):
    # Primary key (unique ID for each user)
    id = db.Column(db.Integer, primary_key=True)

    # User's email (must be unique)
    email = db.Column(db.String(150), unique=True)

    # User's password
    password = db.Column(db.String(150))

    # User's first name
    first_name = db.Column(db.String(150))

    # Relationship: one user can have many notes
    notes = db.relationship('Note')