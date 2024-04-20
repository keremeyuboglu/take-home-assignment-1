from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from app.menu_items.routes import menu_item_controller
from app.menus.routes import menu_controller
from .seed import seed_data_if_unseeded
from .database import db
from dotenv import load_dotenv
import os

def create_app(config=None):
    load_dotenv()
    config= os.environ
    print(config)
    # create and configure the app
    database_credentials = {
        'dbname': config['POSTGRES_DB'],
        'user': config['POSTGRES_USER'],
        'password': config['POSTGRES_PASSWORD'],
        'host': config['POSTGRES_HOST'],
        'port': config['POSTGRES_PORT']
    }

    app = Flask(__name__)
    app.register_blueprint(menu_controller)
    app.register_blueprint(menu_item_controller)
    connection_string = "postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}".format(**database_credentials)
    print(rf"Connection Str:{connection_string}")
    app.config["SQLALCHEMY_DATABASE_URI"] = connection_string
    db.init_app(app)  

    seed_data_if_unseeded(app)
    return app



