# -*- coding: UTF-8 -*-

from flask import Flask, g
from flask import url_for
from flask import redirect

from .home import home
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


@app.route('/')
def index():
    return redirect(url_for('home.homepage'))
