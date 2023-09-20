#!/usr/bin/python3
"""A script that starts a Flask web application"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!' in the route /"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays 'HBNB' in the route /hbnb"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Displays 'C' followed by the value of the text variable"""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py_text(text):
    """Displays 'Python' followed by the value of the text variable"""
    return 'Python {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
