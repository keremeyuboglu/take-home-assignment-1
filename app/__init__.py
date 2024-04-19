from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from .routes import menu_controller
from .seed import *
from .database import db


def create_app(test_config=None):
    # create and configure the app
    database_credentials = {
        'dbname': 'Unplug',
        'user': 'postgres',
        'password': '123',
        'host': 'localhost',
        'port': '5432'
    }

    app = Flask(__name__)
    app.register_blueprint(menu_controller)
    connection_string = "postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}".format(**database_credentials)
    app.config["SQLALCHEMY_DATABASE_URI"] = connection_string
    db.init_app(app)  

    seed_data_if_unseeded(app)
    return app



