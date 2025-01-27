from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, JWTManager
from app import app

auth_routes = Blueprint("auth_routes", __name__)
app.config['JWT_SECRET_KEY'] = "your_secret_key"  # Use a secure secret key
jwt = JWTManager(app)

# Mock user data
users = {
    "test@tutoring.com": "password"
}

@auth_routes.route('/api/register', methods=['POST'])
def register():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if email in users:
        return jsonify({"message": "Email already exists!"}), 400

    users[email] = password
    return jsonify({"message": "User registered successfully!"}), 201

@auth_routes.route('/api/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if users.get(email) == password:
        token = create_access_token(identity=email)
        return jsonify({"access_token": token}), 200

    return jsonify({"message": "Invalid credentials"}), 401

@auth_routes.route('/api/secure', methods=['GET'])
@jwt_required()
def secure():
    return jsonify({"message": "Access granted!"}), 200
