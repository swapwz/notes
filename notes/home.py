# -*- coding: utf-8 -*-
import os

from flask import Blueprint
from flask import render_template
from flask import send_from_directory

bp = Blueprint('home', __name__, url_prefix='/home')


@bp.route('/')
def index():
    # get all notes from the DB
    notes = ["晚上18点20分准时在楼下等你"]
    return render_template('home/home.html', notes=notes)
