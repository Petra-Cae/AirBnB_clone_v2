#!/usr/bin/python3
"""
Starts a Flask web application that listens on 0.0.0.0:5000
Routes:
    /cities_by_states: HTML page with a list of all states and related cities
"""
from models import storage
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """
    Returns a HTML page with a list of all states and related cities
    sorted by name
    """
    states = storage.all("State")
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown(curr):
    """Tears down the current SQLAlchemy session """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
