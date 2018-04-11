# -*- coding: UTF-8 -*-
from flask import ( 
    Blueprint, request, render_template, 
    send_from_directory, redirect, url_for
)

bp = Blueprint('note', __name__, url_prefix='/note')


@bp.route('/', methods=['GET', 'POST'])
def publish():
    """ Jump to the publish page default """
    if request.method == 'POST':
        content = request.form['content']
        print("Get content", content)
        return redirect(url_for('home.index'))
    return render_template('note/publish.html')
