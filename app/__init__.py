from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options


config_name = "development"

app = Flask (__name__, instance_relative_config=True)
app.config.from_object(config_options[config_name])
app.config.from_pyfile('config.py')

bootstrap = Bootstrap(app)

from .main import main as main_blueprint
app.register_blueprint(main_blueprint)

# from . import views