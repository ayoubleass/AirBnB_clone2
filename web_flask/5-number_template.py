#!/usr/bin/python3
"""This script setup a Flask web application  on 0.0.0.0, port 5000"""

from flask import Flask
from flask import render_template
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


@app.route('/python/', strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def py_text(text='is cool'):
    """Displays <text>"""
    content = "Python " + text.replace('_', ' ')
    return content


@app.route("/number/<int:n>")
def show_number(n):
    """ display “n is a number” only if n is an integer"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def show_template(n):
    """Displays  a HTML page only if <n< is an integer """
    return render_template('5-number.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
