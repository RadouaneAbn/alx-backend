#!/usr/bin/env python3
""" This module is flask app that serves one route '/' """
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Any, List
import pytz

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

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
    if locale and locale in app.config['LANGUAGES']:
        return locale
    if g.user:
        locale = g.user.get("locale")
        if locale and locale in app.config["LANGUAGES"]:
            return locale
    locale = request.headers.get('locale', "")
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """ This functino gets the timezone of a user """
    timezone = request.args.get("timezone", None)
    if not timezone and g.user:
        timezone = g.user.get("timezone")
    try:
        return pytz.timezone(timezone).zone
    except pytz.exceptions.UnknownTimeZoneError:
        return app.config['BABEL_DEFAULT_TIMEZONE']


def get_user():
    """ This function return a user if found """
    user_id = request.args.get('login_as', type=int)
    return users.get(user_id, None)


@app.before_request
def before_request():
    """ This function is executed before request to check if
    a user is logged in """
    g.user = get_user()


@app.route("/", methods=["GET"])
def root() -> Any:
    """ This is the root/home page """
    return render_template("7-index.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
