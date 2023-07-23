#!/usr/bin/python3
""" starts a Flask web application """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ Returns a greeting from 0.0.0.0:5000 """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Returns HBNB from 0.0.0.0:5000/hbnb """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """
    Returns C followed by the value of the text var
    """
    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route('/python/(<text>)', strict_slashes=False)
def python_is_cool(text="is cool"):
    """
    Returns Python followed by the value of the text var
    """
    text = text.replace('_', ' ')
    return "Python {}".format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0')