from flask import request, jsonify, session
from models.user import User

def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()

    if user is None or not user.check_password(password):
        return jsonify({"message": "Invalid email or password"}), 401

    session['user_id'] = user.id
    return jsonify({"message": "Login successful!"}), 200
