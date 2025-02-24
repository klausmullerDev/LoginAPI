from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

routes_bp = Blueprint("routes", __name__)

@routes_bp.route("/dados_protegidos", methods=["GET"])
@jwt_required()
def dados_protegidos():
    current_user = get_jwt_identity()
    return jsonify({"username": current_user})
