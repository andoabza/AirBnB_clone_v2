#!/usr/bin/python3
"""A python script that starts a Flask web application"""

from flask import Flask, render_template, request, jsonify
from models import storage
from models.state import State
from os import getenv

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Display a HTML page: (inside the tag BODY)"""
    # H1 tag: "States" inside the tag BODY
    # UL tag: with the list of all State objects present in DBStorage
    # LI tag: description of one State: <state.id>: <B><state.name></B>
    # sorted by name (A->Z)
    states = storage.all(State).values()
    states_sorted = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=states_sorted)


@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
