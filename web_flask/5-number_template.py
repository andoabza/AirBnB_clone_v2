#!/usr/bin/python3
"""A python script that starts a Flask web application"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Display Hello HBNB! from the root route /"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display HBNB from the route /hbnb"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """Display C {...} from the route /c/<text>"""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """Display Python {...} from the route /python/<text>"""
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Display n is a number only if n is an integer"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Display a HTML page only if n is an integer"""
    # H1 tag: "Number: n" inside the tag BODY
    return render_template('5-number.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
