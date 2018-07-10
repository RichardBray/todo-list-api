from app import app
from db import db

db.init_app(app)


def create_tables():
    db.create_all()
