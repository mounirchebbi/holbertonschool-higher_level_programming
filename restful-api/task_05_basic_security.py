#!/usr/bin/python3
"""Flask webserver with Basic Authentication"""

from flask import Flask, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
basic_auth = HTTPBasicAuth()

# Users stored in memory with username, hashed password, and role
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


# B.A password verification
@basic_auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users[username]["password"], password):
        return username
    return None


# B.A error handler
@basic_auth.error_handler
def error_handler():
    return jsonify("401 Unauthorized"), 401


# Protected route with Basic Authentication
@app.route("/basic-protected")
@basic_auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


if __name__ == "__main__":
    app.run(debug=True)  # Debug mode for development; remove in production
