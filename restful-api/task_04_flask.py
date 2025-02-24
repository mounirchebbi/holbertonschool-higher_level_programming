#!/usr/bin/python3
# task_04_flask.py
"""implementation of flask webserver"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory users dictionary
users = {
    "jane": {"name": "Jane", "age": 28, "city": "Los Angeles"},
    "mark": {"name": "Mark", "age": 35, "city": "Chicago"},
}


# Root route
@app.route("/")
def home():
    return "Welcome to the Flask API!"


# Route to serve user data
@app.route("/data")
def get_data():
    return jsonify(list(users.keys()))  # Returns only usernames


# Status endpoint
@app.route("/status")
def status():
    return "OK"


# Dynamic route for fetching user details
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


# Route to handle adding users via POST request
@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()
    if not data or "username" not in data:
        return jsonify({"error":"Username is required"}), 400

    username = data["username"]
    if username in users:
        return jsonify({"error": "User already exists"}), 400

    users[username] = {
        "name": data["name"],
        "age": data["age"],
        "city": data["city"]
    }

    return jsonify({"message": "User added",
                    "user": users[username]}), 201


# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
