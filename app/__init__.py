from flask import Flask
from .config import Config
from .extensions import db,migrate

from app.clientes.controllers import clientes_api

def create_app():
    app=Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app,db)

    app.register_blueprint(clientes_api)

    return app