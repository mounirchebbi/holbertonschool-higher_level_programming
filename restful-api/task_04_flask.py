#!/usr/bin/python3
# task_04_flask.py
"""implementation of flask webserver"""

from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)
users = {}


@app.route("/")
def home():
    """Root route"""

    return "Welcome to the Flask API!"


@app.route("/data")
def get_data():
    """Route to users data Returns only usernames"""

    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """Status endpoint"""

    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """Dynamic route for fetching user data"""

    if username in users:
        return jsonify(users[username])
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """Route add user via POST request"""

    data = request.get_json()
    if not data or "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]
    if username in users:
        return jsonify({"error": "User already exists"}), 400

    users[username] = {
        "username": username,
        "name": data["name"],
        "age": data["age"],
        "city": data["city"]
    }

    return jsonify({"message": "User added", "user": users[username]}), 201


# Run the Flask app
if __name__ == "__main__":
    app.run()
