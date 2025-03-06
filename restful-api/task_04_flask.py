#!/usr/bin/python3
# task_04_flask.py
"""implementation of flask webserver"""

from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)


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
    if username in users:
        user_data = users[username]
        return jsonify({
            "username": username,
            "name": user_data["name"],
            "age": user_data["age"],
            "city": user_data["city"]
        })
    return jsonify({"error": "User not found"}), 404


# Route add user via POST request
@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()
    if not data or "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]
    if username in users:
        return jsonify({"error": "User already exists"}), 400

    # Store only the required fields
    users[username] = {
        "name": data["name"],
        "age": data["age"],
        "city": data["city"]
    }

    # Return response with username included in user object
    return jsonify({
        "message": "User added",
        "user": {
            "username": username,
            "name": data["name"],
            "age": data["age"],
            "city": data["city"]
        }
    }), 201


# Run the Flask app
if __name__ == "__main__":
    app.run()
