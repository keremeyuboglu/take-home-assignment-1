from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from db_models import * 

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)