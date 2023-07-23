#!/usr/bin/python3
"""
Starts a Flask web application that listens on 0.0.0.0:5000
Routes:
    /hbnb_filters: HTML filter page for HBnB
"""
from models import storage
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """Displays the HBnB filter page"""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template("10-hbnb_filters.html",
                           states=states, amenities=amenities)


@app.teardown_appcontext
def teardown(curr):
    """Ends the current SQLAlchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
