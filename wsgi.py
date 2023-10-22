#!/usr/bin/env python
"""Minimal Litestar application."""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def helloworld():
    return "Hello World From Flask!"


if __name__ == "__main__":
    app.run(port=8081)
