# -*- coding: UTF-8 -*-
from flask import Flask, g
from flask import url_for
from flask import redirect
from flask import render_template


def create_app():
    """Create note instance"""
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('page_not_found.html'), 404

    # database tools
    import db
    @app.before_request
    def before_request():
        g.session = db.get_session()

    @app.teardown_request
    def teardown_request(exception):
        db.put_session()

    # register all blueprints
    from notes import home, upload, note 
    app.register_blueprint(home.bp)
    app.register_blueprint(upload.bp)
    app.register_blueprint(note.bp)

    @app.route('/')
    def index():
        """ Redirect to home page """
        return redirect(url_for('home.index'))

    return app


app = create_app()
