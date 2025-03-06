#!/usr/bin/python3
# task_04_flask.py
"""implementation of flask webserver"""

from flask import Flask
from flask import jsonify

app = Flask(__name__)

# In-memory users dictionary
users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}

# Root route
@app.route("/")
def home():
    return "Welcome to the Flask API!"

# Route to users data Returns only usernames
@app.route("/data")
def get_data():
    return jsonify(list(users.keys()))

# Status endpoint
@app.route("/status")
def status():
    return "OK"


# Dynamic route for fetching user data
@app.route("/users/<username>")
def get_user(username):
    if username and username in users.keys():
        user_data = users.get(username)
        output = {"username": username,
                  "name": user_data["name"],
                  "age": user_data["age"],
                  "city": user_data["city"]}
        return jsonify(output)
    return jsonify({"error": "User not found"}), 404


# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
