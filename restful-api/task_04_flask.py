#!/usr/bin/python3
"""
Flask API that provides basic endpoints to simulate user management.

Available endpoints:
- GET / : Welcome message.
- GET /status : Returns "OK" to confirm the API is running.
- GET /data : Returns a list of all registered usernames.
- GET /users/<username>: Returns the user data for the given username.
- POST /add_user : Adds a new user from JSON data (username, name, age, city).
Users are stored in memory using a dictionary.
"""

from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to the Flask API!"


# Dictionary to store users
users = {}


@app.route("/data")
def get_usernames():
    # Extract only usernames (dictionary keys)
    usernames = list(users.keys())
    return jsonify(usernames)


@app.route("/status")
def status():
    return "OK", 200


@app.route("/users/<username>")
def get_users(username):
    user = users.get(username)
    if user:
        # Use **name_dict to combine dictionaries
        return jsonify({"username": username, **user})
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    # Retrieves the JSON data from the request
    data = request.get_json()

    # Checks if the necessary data is present
    required_fields = {"username", "name", "age", "city"}
    if not data or "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    # Extract username from JSON request
    username = data["username"]
    """if username in users:
        return jsonify({"error": "User already exists"}), 409"""
    # Add user
    users[username] = {
        "name": data["name"],
        "age": data["age"],
        "city": data["city"]
    }

    user_response = {
        "username": username,
        "name": data["name"],
        "age": data["age"],
        "city": data["city"]
    }

    # Returns a confirmation
    return jsonify({
        "message": "User added",
        "user": user_response
    }), 201


if __name__ == "__main__":
    app.run()
