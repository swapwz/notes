# -*- coding: utf-8 -*-
import os

from flask import Blueprint
from flask import render_template
from flask import send_from_directory

import db
import datetime
from model.note import Note

bp = Blueprint('home', __name__, url_prefix='/home')


@bp.route('/')
def index():
    # get all notes from the DB
    session = db.get_session()
    notes = session.query(Note).order_by(Note.id.desc())
    db.put_session()
    msgs = []
    if notes is not None:
        for n in notes:
            msg = dict()
            msg.setdefault('date', n.publish_date.strftime("%Y-%m-%d %H:%M:%S"))
            msg.setdefault('content', n.note)
            msgs.append(msg)
    else:
        msg = dict()
        msg.setdefault('date', '')
        msg.setdefault('content',  u"没有任何信息")
        msgs.append(msg)
    return render_template('home/home.html', msgs=msgs)
