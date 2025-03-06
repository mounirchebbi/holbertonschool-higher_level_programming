#!/usr/bin/python3
# task_04_flask.py
"""implementation of flask webserver"""

from flask import Flask
from flask import jsonify
from flask import request
import json

app = Flask(__name__)


# Root route
@app.route("/")
def home():
    return "Welcome to the Flask API!"


# Route to users data - Returns usernames as a space-separated string
@app.route("/data")
def get_data():
    output = json.dumps(list(users.keys()))
    return (output)


# Status endpoint
@app.route("/status")
def status():
    return "OK"


# Dynamic route for fetching user data with pretty printing
@app.route("/users/<username>")
def get_user(username):
    if username in users:
        user_data = users[username]
        response_data = {
            "username": username,
            "name": user_data["name"],
            "age": user_data["age"],
            "city": user_data["city"]
        }
        # Use json.dumps with indent for pretty printing
        return json.dumps(response_data, indent=4), 200
    return json.dumps({"error": "User not found"}, indent=4), 404


# Route add user via POST request with pretty printing
@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()
    if not data or "username" not in data:
        return json.dumps({"error": "Username is required"}, indent=4), 400

    username = data["username"]
    if username in users:
        return json.dumps({"error": "User already exists"}, indent=4), 400
    users[username] = {
        "name": data["name"],
        "age": data["age"],
        "city": data["city"]
    }

    response_data = {
        "message": "User added",
        "user": {
            "username": username,
            "name": data["name"],
            "age": data["age"],
            "city": data["city"]
        }
    }
    return json.dumps(response_data, indent=4), 201


# Run the Flask app
if __name__ == "__main__":
    app.run()
