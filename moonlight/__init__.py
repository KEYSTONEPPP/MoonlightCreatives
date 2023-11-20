from flask import Flask
from os import path
from flask import render_template

def main_app():
    moon = Flask(__name__)
    moon.config['SECRET_KEY'] = 'creatives art'
    
    from .views import views
    from .auth import auth

    moon.register_blueprint(views, url_prefix='/')
    moon.register_blueprint(auth, url_prefix='/')

    return moon
