from flask import Blueprint, request, jsonify, session, redirect, url_for, render_template
from werkzeug.security import check_password_hash
from models.user import User

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['GET', 'POST'])
def login_user():
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        password = request.form.get('password')

        # 데이터베이스에서 사용자 검색
        user = User.query.filter_by(user_id=user_id).first()

        if user and check_password_hash(user.password_hash, password):
            # 로그인 성공 시 세션에 사용자 ID 저장
            session['user_id'] = user.id
            return redirect(url_for('home'))
        else:
            # 로그인 실패 시 다시 로그인 페이지로 이동하고 오류 메시지 전달
            return render_template('login.html', error="Invalid user ID or password")

    return render_template('login.html')
