#!/usr/bin/python3
""" a script that import from storage"""
from flask import Flask, render_template
from models import storage


app = Flask(__name__)
strict_slashes = False


@app.route('/states_list')
def states_list():
    """ a routte to return alll stayes"""
    states = storage.all("State")
    #sorted_states = sorted(states.values(), key=lambda x: x.name)

    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """ close the storge"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
