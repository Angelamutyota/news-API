from flask import Flask
from .config import config_options

config_name = "development"

app = Flask (__name__)
app.config.from_object(config_options[config_name])

@app.route('/')
def index():
    return '<h2>hello world</h2>'