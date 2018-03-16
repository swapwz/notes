import os

from flask import render_template
from flask import send_from_directory

from . import home


@home.route('/')
def homepage():
    # get all notes from the DB
    notes = ["Ni hao shi jie", "hello world"]
    
    return render_template('home.html', notes=notes)


@home.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(home.root_path, 'static'), 
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
