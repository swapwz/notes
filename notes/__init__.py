# -*- coding: UTF-8 -*-

from flask import Flask, g
from flask import url_for
from flask import redirect

# home page
from .home import home
# upload 
from .upload import upload 

from .model import db


app = Flask(__name__)
app.config.from_pyfile('config.py')

@app.before_request
def before_request():
    g.session = db.get_session(app.config['DATABASE'])


@app.teardown_request
def teardown_request(exception):
    db.put_session()

app.register_blueprint(home, url_prefix="/home")
app.register_blueprint(upload, url_prefix="/upload")

@app.route('/')
def index():
    return redirect(url_for('home.homepage'))
