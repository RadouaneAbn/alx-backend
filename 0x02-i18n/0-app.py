#!/usr/bin/env python3
""" This module is flask app that serves one route '/' """
from flask import Flask, render_template
from typing import Any


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/", methods=["GET"])
def root() -> Any:
    """ This is the root/home page """
    return render_template("0-index.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
