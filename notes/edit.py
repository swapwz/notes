# -*- coding: UTF-8 -*-
from flask import Blueprint
from flask import render_template
from flask import send_from_directory

bp = Blueprint('edit', __name__, url_prefix='/edit')


@bp.route('/')
def index():
    """ Jump to the edit """
    return render_template('edit/edit.html')
