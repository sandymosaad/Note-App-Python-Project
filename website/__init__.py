# Import Flask framework and the SQLAlchemy library for database handling
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

# Initialize SQLAlchemy (database handler)
db = SQLAlchemy()

# Define the name of the database file
DB_NAME = "database.db"


# Function to create and configure the Flask app
def create_app():
    # Create a Flask app instance
    app = Flask(__name__)
    
    # Set a secret key for session management and security
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    
    # Define the database connection URI (SQLite in this case)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    
    # Initialize the SQLAlchemy database with the Flask app
    db.init_app(app)

    # Import blueprints (organized app routes)
    from .views import views
    from .auth import auth

    # Register blueprints with their URL prefixes
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # Import database models (tables)
    from .models import User, Note
    
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()

    # Return the fully configured app instance
    return app


# Function to create a database file if it doesn't exist
def create_database(app):
    # Check if the database file already exists inside the 'website' folder
    if not path.exists('website/' + DB_NAME):
        # Create all tables defined in the models
        db.create_all(app=app)
        print('Created Database!')
