#!/usr/bin/python3
""" print given param as arg"""
from flask import Flask
from flask import render_template

app = Flask(__name__)
app.url_map.strict_slashes=False
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
    if text == None:
        return "Python is cool"
    x = text.replace('_', ' ')
    return f"Python {x}"

@app.route('/number/<n>')
def number(n):
    """ print n if it's number"""
    m = int(n)
    return f"{m} is a number"

@app.route('/number_template/<n>')
def template(n):
    """ render html template"""
    m = int(n)
    return render_template('5-number.html', m=m)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)
