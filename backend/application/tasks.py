# coding=utf-8

from time import sleep
from application import create_app

from lib.flask_sse import sse


def task(arg):
    app = create_app()
    for _ in range(3):
        with app.app_context():
            sse.publish({"message": "this is a pubished SSE from an enqueued task", "arg": arg}, type="sse_from_task")
        sleep(3)
