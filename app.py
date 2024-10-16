# 메인 코드입니다. 
# 이 파일은 절대 지우지 말아주세요 !!!!!

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from auth import login, register  # auth 패키지에서 모듈 가져오기

if __name__ == '__main__':
    print('메인 모듈 실행')
    app.run(debug=True)
