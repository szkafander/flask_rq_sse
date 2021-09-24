# coding=utf-8

from flask import Flask
from flask_cors import CORS
from flask_sse import sse


def create_app():
    app = Flask(__name__)
    app.config["REDIS_URL"] = "redis://localhost"
    CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'
    from application.routes import api
    with app.app_context():
        app.register_blueprint(sse, url_prefix="/stream")
        app.register_blueprint(api)
    return app
