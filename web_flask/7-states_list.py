#!/usr/bin/python3
""" a script that import from storage"""
from flask import Flask
from models import storage
from models.state import State

app = Flask(__name__)
strict_slashes = False


@app.route('/states_list')
def states_list():
    states = storage.all(State)
    sorted_states = sorted(states.values(), key=lambda x: x.name)

    return render_template('7-states_list.html', states=sorted_states)


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
