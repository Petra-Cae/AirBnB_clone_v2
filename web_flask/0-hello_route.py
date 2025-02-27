#!/usr/bin/python3
""" starts a Flask web application """
from flask import Flask
app = Flask(__name__)

# route for AirBnB root URL
@app.route('/airbnb-onepage/', strict_slashes=False)
def hello_hbnb():
    """ Returns a greeting from 0.0.0.0:5000 """
    return "Hello HBNB!"


if __name__ == '__main__':
    """start Flask dev server, listen on all available networks, port 5000"""
    app.run(host='0.0.0.0', port=5000)
