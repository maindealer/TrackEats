from flask import Blueprint, request, jsonify
from extensions import db
from models.user import User
from werkzeug.security import generate_password_hash

register_bp = Blueprint('register', __name__)

@register_bp.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    user_id = data.get('user_id')
    email = data.get('email')
    password = data.get('password')

    hashed_password = generate_password_hash(password)
    new_user = User(user_id=user_id, email=email, password_hash=hashed_password)
    
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully!"}), 201
