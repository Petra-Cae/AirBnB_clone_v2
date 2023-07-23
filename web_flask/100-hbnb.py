#!/usr/bin/python3
""" Starts a Flask application listening on 0.0.0.0:5000 """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.place import Place
from models.amenity import Amenity
app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(curr):
    """ Ends current SqlAlchemy session """
    storage.close()


@app.route('/hbnb/', strict_slashes=False)
def display_html():
    """ Displays filters page """
    states = storage.all(State)
    amenities = storage.all(Amenity)
    places = storage.all(Place)
    return render_template('100-hbnb.html',
                           states=states.values(),
                           amenities=amenities.values(),
                           places=places.values())


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
