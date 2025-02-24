from flask import Blueprint, request, jsonify
from models import User, db
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from flask_cors import CORS
from datetime import datetime, timedelta
import secrets

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

@auth_bp.route("/change_password", methods=["POST"])
@jwt_required()
def change_password():
    data = request.get_json()
    current_user = get_jwt_identity()
    user = User.query.filter_by(username=current_user).first()
    if not user:
        return jsonify({"message": "Usuário não encontrado"}), 404

    old_password = data.get("old_password")
    new_password = data.get("new_password")

    if not user.check_password(old_password):
        return jsonify({"message": "Senha atual incorreta"}), 401

    user.set_password(new_password)
    db.session.commit()
    return jsonify({"message": "Senha alterada com sucesso!"}), 200

@auth_bp.route("/forgot_password", methods=["POST"])
def forgot_password():
    data = request.get_json()
    email = data.get("email")
    user = User.query.filter_by(email=email).first()
    if user:
        reset_token = secrets.token_urlsafe()
        user.reset_token = reset_token
        user.reset_token_expiration = datetime.utcnow() + timedelta(hours=1)
        db.session.commit()
        # Em produção, enviar email com o token. Para teste, retornamos o token.
        return jsonify({"reset_token": reset_token}), 200
    return jsonify({"message": "Se o e-mail existir, um link será enviado."}), 200

@auth_bp.route("/reset_password", methods=["POST"])
def reset_password():
    data = request.get_json()
    reset_token = data.get("reset_token")
    new_password = data.get("new_password")
    user = User.query.filter_by(reset_token=reset_token).first()
    if not user or user.reset_token_expiration < datetime.utcnow():
        return jsonify({"message": "Token inválido ou expirado"}), 400
    user.set_password(new_password)
    user.reset_token = None
    user.reset_token_expiration = None
    db.session.commit()
    return jsonify({"message": "Senha redefinida com sucesso!"}), 200

