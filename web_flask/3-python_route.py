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


@app.route("/c/<text>", strict_slashes=False)
def cText(text):
    """ Dispalys <text>"""
    content = "C " + text.replace('_', ' ')
    return content


@app.route('/python/')
@app.route("/python/<text>", strict_slashes=False)
def py_text(text='cool'):
    """Displays <text>"""
    content = "Python " + text.replace('_', ' ')
    return content


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
