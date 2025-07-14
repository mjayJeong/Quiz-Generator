from flask import Blueprint, request, jsonify
from models import db, User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token

auth_bp = Blueprint('auth', __name__)


# 회원가입 로직
@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    email = data['email']
    password = data['password']
    confirm = data['confirmPassword']
    name = data['name']
    birthdate = data['birthdate']

    if password != confirm:
        return jsonify({'error' : '비밀번호가 일치하지 않습니다.'}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({'error' : '이미 존재하는 이메일입니다.'}), 409
    
    hashed_pw = generate_password_hash(password)
    new_user = User(email=email, password=hashed_pw, name=name, birthdate=birthdate)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': '회원가입 성공!'}), 201


# 로그인 로직
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data['email']
    password = data['password']
    
    user = User.query.filter_by(email=email).first()
    if user and check_password_hash(user.password, password):
        token = create_access_token(identity=email)
        return jsonify({'token': token})
    return jsonify({'error': '로그인에 실패하였습니다.'}), 401