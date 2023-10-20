#!/usr/bin/python3
""" print given param as arg"""
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello():
    """ print “Hello HBNB!”"""

    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """ print in route hbnb"""

    return "HBNB"


@app.route('/c/<text>')
def c(text):
    """ print text using text"""
    x = text.replace('_', ' ')

    return f"C {x}"


@app.route('/python')
@app.route('/python/<text>')
def python(text=None):
    """ print text using python"""
    if text is None:

        return "Python is cool"
    x = text.replace('_', ' ')
    return f"Python {x}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
