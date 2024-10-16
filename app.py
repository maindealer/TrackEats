from flask import Flask, request, jsonify, session
from werkzeug.security import check_password_hash
from models import User  # User 모델을 가져옴
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # 세션에 필요한 시크릿 키 설정
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # 데이터베이스 설정

db = SQLAlchemy(app)

# 로그인 함수
@app.route('/login', methods=['POST'])
def login():
    # 1. 사용자가 입력한 이메일과 비밀번호를 받아옴
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    # 2. DB에서 해당 이메일을 가진 사용자가 있는지 찾음
    user = User.query.filter_by(email=email).first()

    if user is None:
        return jsonify({"message": "Invalid email or password"}), 401

    # 3. 비밀번호 검증 (DB의 해시된 비밀번호와 비교)
    if not check_password_hash(user.password, password):
        return jsonify({"message": "Invalid email or password"}), 401

    # 4. 세션에 사용자 정보 저장 (또는 JWT 토큰 생성)
    session['user_id'] = user.id
    return jsonify({"message": "Login successful!"})

if __name__ == '__main__':
    app.run(debug=True)
