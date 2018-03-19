# -*- coding: UTF-8 -*-
import os

from flask import render_template
from flask import send_from_directory

from . import home


@home.route('/')
def homepage():
    # get all notes from the DB
    notes = ["Xiao Hua", 
             "Hello",
             "You are very beautiful",
             "Time is fly",
             "Have your fun."]
    
    return render_template('home.html', notes=notes)


@home.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(home.root_path, 'static'), 
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
