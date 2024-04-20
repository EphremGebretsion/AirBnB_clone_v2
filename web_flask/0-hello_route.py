#!/usr/bin/python3
"""display hello using flask"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def display():
    """returns to the root route or /"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
