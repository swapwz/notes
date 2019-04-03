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


def delete_msg(msg_id):
    session = db.get_session()
    msg = session.query(Note).filter(Note.id==msg_id).first()
    if msg:
        session.delete(msg)
        session.commit()
    return


def total_count():
    session = db.get_session()
    count = session.query(Note).count()
    db.put_session()
    return count


def get_msgs(offset, limit=MAX_MSGS):
    session = db.get_session()
    notes = session.query(Note).order_by(Note.id.desc()).offset(offset).limit(limit)
    db.put_session()
    msgs = []
    if notes is not None:
        for n in notes:
            msg = dict()
            msg.setdefault('id', str(n.id))
            msg.setdefault('date', n.publish_date.strftime("%Y-%m-%d %H:%M:%S"))
            msg.setdefault('content', n.note)
            msgs.append(msg)
    return msgs


@bp.route('/')
def index():
    count = total_count()
    print "total count is %s" % count
    # get all notes from the DB
    msgs = get_msgs(0)
    if msgs and len(msgs) == 0:
        msg = dict()
        msg.setdefault('date', '')
        msg.setdefault('content',  u"没有任何信息")
        msgs.append(msg)
    return render_template('home/home.html', msgs=msgs, count=count)


@bp.route('/next')
def next():
    offset = request.args.get('offset')
    count = total_count()
    msgs = get_msgs(offset)
    if msgs and len(msgs) == 0:
        msg = dict()
        msg.setdefault('id', '')
        msg.setdefault('date', '')
        msg.setdefault('content',  u"哥，真的没了")
        msgs.append(msg)
    return render_template('home/home.html', msgs=msgs, count=count)


@bp.route('/delete')
def delete():
    msg_id = int(request.args.get('id'))
    delete_msg(msg_id)
    return next()




