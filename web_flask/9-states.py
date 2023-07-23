#!/usr/bin/python3
"""
Starts a Flask web application that listens on 0.0.0.0:5000
Routes:
    /states: a HTML page with a list of all States
    /states/<id>: HTML page that displays the given state with <id>
"""
from models import storage
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """
    Displays an HTML page with a list of all States sorted by name
    """
    states = storage.all("State")
    return render_template("9-states.html", state=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """
    Displays a HTML page with info about the state with <id>, if it exists
    """
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown(curr):
    """Ends the current SQLAlchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
