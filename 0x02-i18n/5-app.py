#!/usr/bin/env python3
"""
This file we'll Create a single
/ route and an index.html template that simply outputs
“Welcome to Holberton” as page title (<title>)
and “Hello world” as header (<h1>)
"""
from flask_babel import Babel
from flask import Flask, render_template, request, g


class Config:
    """This class has a LANGUAGES class attribute
    equal to ["en", "fr"]"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """return user dict or None"""
    login_id = request.args.get('login_as', type=int)
    if login_id:
        return users.get(login_id)
    return None


@app.before_request
def before_request() -> None:
    """Executed before each req"""
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """Gets locale for a web page"""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user.get('locale')
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """renders 0-index.html"""
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)