#!/usr/bin/python3
"""A python script that starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def states(state_id=None):
    """Display a HTML page: (inside the tag BODY)
       -> h1: "States"
       -> ul: list of all 'State' objects present in 'DBStorage'
              sorted by name (A-Z)
            -> li: description of one 'State':
                   "<state.id>: <b><state.name><b>"

       for /states/<id> route: displays a HTML page: (inside the <body> tag)
       if a 'State' object is found with this 'id':
       -> h1: "State"
       -> h3: "Cities:"
            -> ul: list of 'City' objects linked to the 'State'
                   sorted by name (A->Z)
            -> li: description of one 'City':
                   "<city.id>: <b><city.name></b>"
       otherwise:
       -> h1: "Not found!"
    """
    states = storage.all(State)
    if state_id is not None:
        state_id = 'State.' + state_id
    return render_template("9-states.html", states=states, state_id=state_id)


@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
