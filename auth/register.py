from flask import request, jsonify
from werkzeug.security import generate_password_hash
from app import db
from models.user import User

def register():
    data = request.get_json()
    user_id = data.get('user_id')
    email = data.get('email')
    password = data.get('password')
    
    # 비밀번호 해싱
    hashed_password = generate_password_hash(password)
    
    # 새 사용자 생성
    new_user = User(user_id=user_id, email=email, password_hash=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully!"}), 201
