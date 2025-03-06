#!/usr/bin/python3
# task_04_flask.py
"""implementation of flask webserver"""

from flask import Flask

app = Flask(__name__)

# Root route
@app.route("/")
def home():
    return "Welcome to the Flask API!"

# Run the Flask app
if __name__ == "__main__":
    app.run()
