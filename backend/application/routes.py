# coding=utf-8

from flask import Blueprint, current_app
from flask.json import jsonify
from redis import Redis
from rq import Queue

from application.tasks import task
from lib.flask_sse import sse

api = Blueprint("rest", __name__)

q = Queue(connection=Redis())


@api.route("/api_test")
def api_test():
    return jsonify({"message": "this is returned by the /api_test route"})


@api.route("/sse_test")
def sse_test():
    with current_app.app_context():
        sse.publish({"message": "this is from a published SSE"}, type="sse_test")
    return jsonify({"message": "this is returned by the /sse_test route"})


@api.route("/queue_test")
def queue_test():
    q.enqueue(task, "this argument was passed by the caller")
    return jsonify({"message": f"this is returned by the /queue_test route"})
    