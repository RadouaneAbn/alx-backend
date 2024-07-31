#!/usr/bin/env python3
""" This module is flask app that serves one route '/' """
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Any, List


app = Flask(__name__)
app.url_map.strict_slashes = False


class Config:
    """ The configuration class for the Flask app """
    LANGUAGES: List[str] = ["en", "fr"]
    BABEL_DEFAULT_LOCALE: str = "en"
    BABEL_DEFAULT_TIMEZONE: str = "UTC"


app.config.from_object(Config)
babel: Babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """ Select the best match locale based on the Accept-Language header """
    locale = request.args.get("locale")
    if locale and locale in Config.LANGUAGES:
        return locale

    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route("/", methods=["GET"])
def root() -> Any:
    """ This is the root/home page """
    return render_template("4-index.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
