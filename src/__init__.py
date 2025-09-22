from flask import Flask
from flask_restful import Api
from src.routes.endpoints import initialize_endpoints
from src.model.Base import db

def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://usuario:senha@localhost:5432/concessionaria'
  #  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Para evitar avisos desnecessários
    db.init_app(app)

    # Flask API
    api = Api(app, prefix="/api")
    initialize_endpoints(api)


   # app.debug = True  # Habilita o modo de depuração
    return app
