#!/usr/bin/python3
"""flask web app with route / and /hbnb"""
from flask import Flask, render_template
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


@app.route("/python", strict_slashes=False)
def pythonRouteDefault():
    """display Python is cool to /python route"""
    return f"Python is cool"


@app.route("/python/<text>", strict_slashes=False)
def pythonRoute(text):
    """displays Python <text>"""
    tx = text.replace("_", " ")
    return f"Python {tx}"


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """displays <n> is a number"""
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def numberTemp(n):
    """displays Number: <n> as h1"""
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
