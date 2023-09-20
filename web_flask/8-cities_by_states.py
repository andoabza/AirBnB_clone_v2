#!/usr/bin/python3
"""A python script that starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Display a HTML page: (inside the tag BODY)"""
    # H1 tag: "States" inside the tag BODY
    # UL tag: with the list of all State objects present in DBStorage
    # LI tag: description of one State: <state.id>: <B><state.name></B>
    # LI tag: description of one City: <city.id>: <B><city.name></B>
    # sorted by name (A->Z)
    states = storage.all(State)
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
