#!/usr/bin/python3
'''
First program using Flask framework
'''
from flask import Flask, render_template, g
from models import storage
from models.state import State
import json

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_db(exception):
    '''Close connection'''
    storage.close()


@app.route('/states_list')
def states_list():
    '''List all States'''

    states = []
    for k, v in storage.all(State).items():
        states.append(v.to_dict())
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(debug=True)
