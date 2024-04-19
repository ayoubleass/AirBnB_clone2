#!/usr/bin/python3
"""This script setup a Flask web application  on 0.0.0.0, port 5000"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def default():
    """This functions displays the default content."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Display HBNB"""
    return "HBNB"


@app.route("/c/<text>")
def cText(text):
    """ Dispalys <text>"""
    content = text.replace('_', ' ')
    return content


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
