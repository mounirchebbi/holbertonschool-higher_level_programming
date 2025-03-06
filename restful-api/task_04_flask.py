#!/usr/bin/python3
# task_04_flask.py
"""implementation of flask webserver"""

from flask import Flask
from flask import jsonify

app = Flask(__name__)

# In-memory users dictionary
#users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}

# Root route
@app.route("/")
def home():
    return "Welcome to the Flask API!"

# Route to users data Returns only usernames
@app.route("/data")
def get_data():
    return jsonify(list(users.keys()))

# Run the Flask app
if __name__ == "__main__":
    app.run()
