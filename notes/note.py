#-*- coding: UTF-8 -*-

from flask import ( 
    Blueprint, request, render_template, 
    send_from_directory, redirect, url_for
)

import datetime
import config
import db

from model import note as n


bp = Blueprint('note', __name__, url_prefix='/note')


@bp.route('/', methods=['GET', 'POST'])
def publish():
    """ Jump to the publish page default """
    if request.method == 'POST':
        content = request.form.get('content')
        currentDT = datetime.datetime.now()
        msg = n.Note(note=content, publish_date=currentDT, user_id=0, visits=0)
        session = db.get_session()
        if session:
            session.add(msg)
            session.commit()
            db.put_session()
        return redirect(url_for('home.index'))
    return render_template('note/publish.html')
