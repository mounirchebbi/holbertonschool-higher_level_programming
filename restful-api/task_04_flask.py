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


@app.route('/data')
def get_data():
    """Route to users data Returns only usernames"""

    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    """Status endpoint"""

    return "OK"


@app.route('/users/<username>')
def get_user_info(username):
    """route for fetching user data"""

    if username in users:
        return jsonify(users[username])
    return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """Route add user via POST request"""
    userdata = request.get_json()
    username = userdata.get('username')
    if not username:
        return jsonify({"error": "Username is required"}), 400
    users[username] = {
        'username': username,
        'name': userdata.get('name'),
        'age': userdata.get('age'),
        'city': userdata.get('city')
    }

    return jsonify({"message": "User added", "user": users[username]}), 201


if __name__ == "__main__":
    app.run()
