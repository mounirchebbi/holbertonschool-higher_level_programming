#!/usr/bin/python3
"""Flask webserver with Basic Authentication"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, jwt_required
from flask_jwt_extended import create_access_token, get_jwt_identity
import datetime


app = Flask(__name__)
basic_auth = HTTPBasicAuth()

# JWT configuration
app.config['JWT_SECRET_KEY'] = 'my-secret-key'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(hours=1)
jwt = JWTManager(app)


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


# Login route to get JWT token
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Missing JSON data"}), 400

    username = data.get('username', None)
    password = data.get('password', None)

    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400

    if username not in users or \
            not check_password_hash(users[username]["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    # Create access token with user identity and role
    access_token = create_access_token(
        identity=username,
        additional_claims={"role": users[username]["role"]}
    )

    return jsonify({"access_token": access_token})


if __name__ == "__main__":
    app.run(debug=True)  # Debug mode for development; remove in production
