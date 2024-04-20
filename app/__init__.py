from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from app.menu_items.routes import menu_item_controller
from app.menus.routes import menu_controller
from app.seed import seed_data_if_unseeded
from app.database import db
from app.config import config
from dotenv import load_dotenv
import os

def create_app():
    load_dotenv("./.env")
    app = Flask(__name__)
    app.register_blueprint(menu_controller)
    app.register_blueprint(menu_item_controller)
    app_config =  config[os.environ["FLASK_ENV"]]
    app.config.from_object(app_config)
    db.init_app(app)  
    
    
    with app.app_context() as ctx:
        db.create_all()
        
    seed_data_if_unseeded(app)
    return app



