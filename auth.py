from flask import Blueprint, request, jsonify
from models import User, db
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token
from flask_cors import CORS

bcrypt = Bcrypt()
auth_bp = Blueprint("auth", __name__)
CORS(auth_bp)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if User.query.filter_by(email=email).first():
        return jsonify({"message": "E-mail já cadastrado"}), 400

    new_user = User(username=username, email=email)
    new_user.set_password(password)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "Usuário registrado com sucesso!"}), 201

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    user = User.query.filter_by(email=email).first()
    if not user or not user.check_password(password):
        return jsonify({"message": "Credenciais inválidas"}), 401

    access_token = create_access_token(identity=user.username)
    return jsonify({"access_token": access_token})
