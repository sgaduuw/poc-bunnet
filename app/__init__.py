from flask import Flask
from app.routes.public import public
from bunnet import init_bunnet
from pymongo import MongoClient
from environs import Env

env = Env()
c_mongo = MongoClient(env.str("MONGODB_URL"))

class Config:
    FLASK_DEBUG = True


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)
    register_extensions(app)
    register_blueprints(app)

    init_bunnet(
        database=c_mongo.poc,
        document_models=[
            'app.models.Author',
            'app.models.Post'
        ]
    )
    return app

def register_extensions(app) -> None:
    """Register Flask extensions."""
    return None

def register_blueprints(app) -> None:
    """Register Flask blueprints."""
    app.register_blueprint(public)
    return None

if __name__ == 'main':
    app = create_app()
    app.run()
