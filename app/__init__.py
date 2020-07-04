from flask import Flask
from flask_bootstrap import flask_bootstrap
from config import config_options

bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__)

    # App configuration
    app.config.from_object(config_options[config_name])

    # Init extensions
    bootstrap.init_app(app)

    # Blueprint

    # Setting config

    return app
