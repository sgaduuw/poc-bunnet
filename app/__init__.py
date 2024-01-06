from flask import Flask
from app.routes.public import public

class Config:
    FLASK_DEBUG = True

def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)
    register_extensions(app)
    register_blueprints(app)
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
