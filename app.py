# 메인 코드입니다. 
# 이 파일은 절대 지우지 말아주세요 !!!!!
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config  # 설정 파일 import
from auth import login, register  # 로그인, 회원가입 관련 모듈 import

# Flask 애플리케이션 생성
app = Flask(__name__)

# 설정 적용 (MySQL, SECRET_KEY 등)
app.config.from_object(Config)

# 데이터베이스 및 마이그레이션 설정
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# 라우트 설정 (회원가입과 로그인 기능)
@app.route('/register', methods=['POST'])
def register_user():
    return register.register()  # 회원가입 처리

@app.route('/login', methods=['POST'])
def login_user():
    return login.login()  # 로그인 처리

if __name__ == '__main__':
    app.run(debug=True)  # 애플리케이션 실행
