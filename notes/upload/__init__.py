from flask import Blueprint

upload = Blueprint('upload', __name__,
                   template_folder='templates',
                   static_folder='static')

from . import views
