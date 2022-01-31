#!/usr/bin/python3
'''
First program using Flask framework
'''
from email.policy import default
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_db(exception):
    '''Close connection'''
    storage.close()


@app.route('/states', defaults={'id': ''})
@app.route('/states/<id>')
def states(id):
    '''List all States'''
    sta = storage.all(State)
    states = []
    if id == '':
        return render_template(
            '9-states.html', states=sta, id=id)
    else:
        for v in sta.values():
            if v.id == id:
                states.append(v)
                return render_template(
                    '9-states.html', states=states[0], id=id)
        return render_template(
                        '9-states.html', states=states, id='error')


if __name__ == "__main__":
    app.run(debug=True)
