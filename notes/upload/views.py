# -*- coding: UTF-8 -*-
import os
import dircache

from flask import render_template
from flask import send_from_directory
from flask import request, redirect, url_for
from werkzeug.utils import secure_filename

from . import upload


upload_dir = '/var/www/notes/upload' 


@upload.route('/', methods=['GET', 'POST'])
def index():
    global upload_dir
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(upload_dir, filename))
        return redirect(url_for('upload.show_photo'))
    else:
        return render_template('upload.html')


@upload.route('/showphotos', methods=['GET'])
def show_photo():
    try:
        filenames = dircache.listdir(upload_dir)
        return render_template('filelist.html', filenames=filenames)
    except:
        return redirect(url_for('upload.index'))


@upload.route('/show/<path:filename>')
def show(filename):
    return send_from_directory(upload_dir, filename)



