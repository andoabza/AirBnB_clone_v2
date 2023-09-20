#!/usr/bin/python3
"""A python script that starts a Flask web application"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Display Hello HBNB! from the root route /"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display HBNB from the route /hbnb"""
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
