# -*- coding: utf-8 -*-
import os

from flask import Blueprint
from flask import render_template
from flask import send_from_directory

bp = Blueprint('home', __name__, url_prefix='/home')


@bp.route('/')
def index():
    # get all notes from the DB
    notes = ["Xiao Hua", 
             "Hello",
             "You are very beautiful",
             "Time is fly",
             "Have your fun."]
    return render_template('home/home.html', notes=notes)


@bp.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(bp.root_path, 'static'), 
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
