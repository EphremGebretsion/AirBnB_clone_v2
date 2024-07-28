#!/usr/bin/python3
"""flask web app with route / and /hbnb"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def display():
    """display hello hbhb"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ returns HBNB to route /hbnb"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def croute(text):
    """displays C <tect> the url after c/"""
    tx = text.replace("_", " ")
    return f"C {tx}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
