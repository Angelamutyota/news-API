from flask import Flask
from flask_bootstrap import Bootstrap
from .config import config_options
from app import error


config_name = "development"

app = Flask (__name__, instance_relative_config=True)
app.config.from_object(config_options[config_name])

bootstrap = Bootstrap(app)

from . import views