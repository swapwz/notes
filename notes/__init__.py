# -*- coding: UTF-8 -*-

from flask import Flask, g

from .home import home
from .model import db


app = Flask(__name__)
app.config.from_pyfile('config.py')

@app.before_request
def before_request():
    g.db = db.connect(app.config['DATABASE'])


@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.dispose()


app.register_blueprint(home)
