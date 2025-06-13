#!/usr/bin/python3
"""
Application Flask de démonstration avec authentification sécurisée.

Ce script met en œuvre deux types d'authentification :
1. L'authentification HTTP basique pour accéder à une route protégée.
2. L'authentification basée sur JWT (JSON Web Token)
pour sécuriser l'accès aux API.

Fonctionnalités principales :
- Vérification des identifiants utilisateurs avec mots de passe hachés.
- Route `/login` : génère un token JWT si les identifiants sont valides.
- Route `/basic-protected` : protégée par authentification HTTP basique.
- Route `/jwt-protected` : accessible uniquement avec un token JWT valide.
- Route `/admin-only` : accessible uniquement
par les utilisateurs ayant le rôle "admin".
"""
from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required,
    get_jwt_identity, get_jwt
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

# Clé secrète pour signer les tokens
app.config["JWT_SECRET_KEY"] = "super-secret-key"

# Initialisation de JWT
jwt = JWTManager(app)

# Liste des utilisateurs avec mot de passe haché et rôle
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


# Vérification des identifiants
@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(
       users.get(username).get("password"), password):
        return username
    else:
        return None


# Route protégée par authentification basique
@app.route("/basic-protected", methods=['GET'])
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


# Créer une route /login pour générer le token JWT
@app.route("/login", methods=['POST'])
def login():
    username = request.json.get("username")
    password = request.json.get("password")
    log = verify_password(username, password)

    if log is None:
        return jsonify({"error": "invalid credentials"}), 401
    else:
        access_token = create_access_token(
            identity=username,
            additional_claims={"role": users[username]["role"]})
        return jsonify(access_token=access_token)


# Protéger une route avec JWT
@app.route("/jwt-protected", methods=['GET'])
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"


# Route protégée basée sur les rôles
@app.route("/admin-only", methods=['GET'])
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()  # pour retrouver son nom d’utilisateur
    user_data = users.get(current_user)  # regarde le rôle associé

    if not user_data or user_data.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    else:
        return "Admin Access: Granted"


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run(debug=True)
