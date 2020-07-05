from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

from flask import Blueprint
main = Blueprint('main', __name__)
from . import views, errors

def create_app(config_name):
    app = Flask(__name__)

    # App config
    app.config.from_object(config_options[config_name])

    # Extension init
    bootstrap.init_app(app)

    # Registrering blueprints
    from ..main import main as main_blueprint

    app.register_blueprint(main_blueprint)

    return app