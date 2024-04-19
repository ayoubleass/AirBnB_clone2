#!/usr/bin/env python3
"""
This script setup a Flask web application  on 0.0.0.0, port 5000
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def default():
    return "Hello HBNB!"
