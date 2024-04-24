#!/usr/bin/python3
"""This script setup a Flask web application  on 0.0.0.0, port 5000"""


from flask import Flask
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def each_state_cities():
    """display the states and cities"""
    from models import state
    states = sorted(storage.all(state.State).values(), key=lambda s: s.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_storage(exception):
    """colse the storage"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
