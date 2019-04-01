# -*- coding: utf-8 -*-
import os

from flask import Blueprint
from flask import render_template
from flask import send_from_directory
from flask import request

import db
import datetime
from model.note import Note


MAX_MSGS = 10

bp = Blueprint('home', __name__, url_prefix='/home')


def get_msgs(offset, limit):
    session = db.get_session()
    notes = session.query(Note).order_by(Note.id.desc()).offset(offset).limit(limit)
    db.put_session()
    msgs = []
    if notes is not None:
        for n in notes:
            msg = dict()
            msg.setdefault('date', n.publish_date.strftime("%Y-%m-%d %H:%M:%S"))
            msg.setdefault('content', n.note)
            msgs.append(msg)
    return msgs


@bp.route('/')
def index():
    # get all notes from the DB
    msgs = get_msgs(0, MAX_MSGS)
    if msgs and len(msgs) == 0:
        msg = dict()
        msg.setdefault('date', '')
        msg.setdefault('content',  u"没有任何信息")
        msgs.append(msg)
    return render_template('home/home.html', msgs=msgs)

@bp.route('/next')
def next():
    offset = request.args.get('offset')
    msgs = get_msgs(offset, MAX_MSGS)
    if msgs and len(msgs) == 0:
        msg = dict()
        msg.setdefault('date', '')
        msg.setdefault('content',  u"真的没了")
        msgs.append(msg)
    return render_template('home/home.html', msgs=msgs)


