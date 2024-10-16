from flask import request, jsonify, session
from werkzeug.security import check_password_hash
from models.user import User

def login():
    data = request.get_json()
    user_id = data.get('user_id')
    password = data.get('password')

    # 사용자 찾기
    user = User.query.filter_by(user_id=user_id).first()
    
    if user is None or not check_password_hash(user.password_hash, password):
        return jsonify({"message": "Invalid credentials"}), 401

    # 로그인 성공, 세션에 사용자 ID 저장
    session['user_id'] = user.id
    return jsonify({"message": "Login successful!"}), 200
