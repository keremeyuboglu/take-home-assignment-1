from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from app.seed import seed_data_if_unseeded
from app.database import db
from app.config import config
from flask_marshmallow import Marshmallow
from dotenv import load_dotenv
import os
from apifairy import APIFairy

ma = Marshmallow()
apifairy = APIFairy()


def create_app():
    load_dotenv()
    app = Flask(__name__)
    
    # Register Controllers
    from app.menu_items.routes import menu_item_controller
    from app.menus.routes import menu_controller
    app.register_blueprint(menu_controller)
    app.register_blueprint(menu_item_controller)
    
    
    # Config
    app_config =  config[os.environ["FLASK_ENV"]]
    app.config.from_object(app_config)
    
    # Init dependency libs
    apifairy_init(app)
    db.init_app(app)  
    ma.init_app(app)
    apifairy.init_app(app)
    
    # Create tables if not exists
    with app.app_context() as ctx:
        db.create_all()
        
    # Seed data if unseeded
    seed_data_if_unseeded(app)
    return app

def apifairy_init(app):
    app.config['APIFAIRY_UI'] = 'swagger_ui'
    app.config['APIFAIRY_TITLE'] = 'Unplug Take Home'
    app.config['APIFAIRY_VERSION'] = '1.0'



