# -*- coding: UTF-8 -*-

from flask import Flask, g

from .home import home
from .model import db


app = Flask(__name__)
app.config.from_pyfile('config.py')
db_path = app.config['SQLITE_DB_PATH']


@app.before_request
def before_request():
    g.db = db.connect(db_path)


@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()


app.register_blueprint(home)
