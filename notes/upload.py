# -*- coding: utf-8 -*-
import os
import dircache

from flask import Blueprint
from flask import render_template
from flask import send_from_directory
from flask import request, redirect, url_for

from werkzeug.utils import secure_filename


bp = Blueprint('upload', __name__, url_prefix='/upload')

UPLOAD_DIR = '/var/www/notes/upload' 


@bp.route('/', methods=['GET', 'POST'])
def index():
    global upload_dir
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_DIR, filename))
        return redirect(url_for('upload.show_photo'))
    else:
        return render_template('upload/upload.html')


@bp.route('/showphotos', methods=['GET'])
def show_photo():
    try:
        filenames = dircache.listdir(UPLOAD_DIR)
        return render_template('upload/filelist.html', filenames=filenames)
    except:
        return redirect(url_for('upload.index'))


@bp.route('/show/<path:filename>')
def show(filename):
    return send_from_directory(upload_dir, filename)



