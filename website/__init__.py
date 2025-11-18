from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__) 
    app.config['SECRET_KEY'] = 'your_secret_key_here'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views # Import the views blueprint
    from .auth import auth # Import the auth blueprint

    app.register_blueprint(views, url_prefix='/') # Register the views blueprint
    app.register_blueprint(auth, url_prefix='/') # Register the auth blueprint

    from .models import User, Note  # Import the database models

    create_database(app)

    return app  

def create_database(app): ## Create the database if it doesn't exist
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print('created Database !')