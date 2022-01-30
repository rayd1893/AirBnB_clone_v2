#!/usr/bin/python3
'''
First program using Flask framework
'''
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_db(exception):
    '''Close connection'''
    storage.close()


@app.route('/cities_by_states')
def cities_by_states():
    '''List all States'''

    return render_template(
        '8-cities_by_states.html', states=storage.all(State))


if __name__ == "__main__":
    app.run(debug=True)
