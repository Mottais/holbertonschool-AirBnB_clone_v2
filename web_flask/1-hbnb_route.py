#!/usr/bin/python3
""" Return html page """
from flask import Flask

app = Flask(__name__)


# Définit une route '/' pour l'URL racine
@app.route("/", strict_slashes=False)
def hello_world():
    """ Retourne Hello HBNB"""
    return "Hello HBNB!"


# Définit une route pour l'URL '/hbnb'
@app.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    """ Retourne HBNB"""
    return "HBNB"


if __name__ == '__main__':
    '''Lance l'application Flask'''
    app.run(host='0.0.0.0', port=5000)
