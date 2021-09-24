# coding=utf-8

from flask import Blueprint, current_app
from flask.json import jsonify
from lib.flask_sse import sse


sse_api = Blueprint("sse", __name__)


@sse_api.route("/sse_test")
def sse_test():
    with current_app.app_context():
        sse.publish({"message": "sse test"}, type="sse_test")
    return jsonify({"message": "sse_test"})
