from flask import Flask, render_template, redirect, url_for, session, request, jsonify
from config import Config
from extensions import db, migrate
from auth.register import register_bp
from auth.login import login_bp
from models.user import User

app = Flask(__name__)
app.config.from_object(Config)
app.config['SECRET_KEY'] = 'your_secret_key_here'

db.init_app(app)
migrate.init_app(app, db)

# Blueprint 등록
app.register_blueprint(register_bp)
app.register_blueprint(login_bp)

@app.route('/')
def home():
    if 'user_id' in session:
        return render_template('home.html')
    return redirect(url_for('login_page'))

@app.route('/login', methods=['GET'])
def login_page():
    return render_template('login.html')

@app.route('/register', methods=['GET'])
def register_page():
    return render_template('register.html')

@app.route('/check_user_id', methods=['POST'])
def check_user_id():
    user_id = request.json.get('user_id')
    user = User.query.filter_by(user_id=user_id).first()
    if user:
        return jsonify({'message': '아이디 중복입니다.', 'status': 'fail'})
    return jsonify({'message': '사용 가능한 아이디입니다.', 'status': 'success'})

if __name__ == '__main__':
    app.run()