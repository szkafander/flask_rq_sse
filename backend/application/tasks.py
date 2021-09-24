# coding=utf-8

from time import sleep
from flask_sse import sse

from application import create_app


def task(arg):
    app = create_app()
    for _ in range(3):
        with app.app_context():
            sse.publish({"message": "this is a pubished SSE from an enqueued task", "arg": arg}, type="sse_from_task")
        sleep(3)
