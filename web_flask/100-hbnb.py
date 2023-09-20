#!/usr/bin/python3
"""A python script that starts a Flask web application"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays html like 6-index.html but with some filters"""
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template('100-hbnb.html', states=states,
                           amenities=amenities)


@app.teardown_appcontext
def teardown_db(exception):
    """Removes the current SQLAlchemy Session ie.
    Closing the database again at the end of the request."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
