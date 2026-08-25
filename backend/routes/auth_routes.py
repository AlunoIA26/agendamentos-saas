from functools import wraps

import jwt
from flask import Blueprint, jsonify, request

from services.auth_service import AuthService


auth_bp = Blueprint("auth", __name__)
service = AuthService()


@auth_bp.route("/api/login", methods=["POST"])
def login():
    try:
        dados = request.get_json()

        email = dados["email"]
        senha = dados["senha"]

        token = service.login(email, senha)

        return jsonify({"token": token}), 200

    except (ValueError, KeyError) as erro:
        return jsonify({"erro": str(erro)}), 401


def token_obrigatorio(funcao):
    @wraps(funcao)
    def wrapper(*args, **kwargs):
        cabecalho = request.headers.get("Authorization")

        if not cabecalho or not cabecalho.startswith("Bearer "):
            return jsonify({"erro": "Token ausente ou invalido."}), 401

        token = cabecalho.split(" ", 1)[1]

        try:
            dados = service.validar_token(token)
        except jwt.InvalidTokenError:
            return jsonify({"erro": "Token ausente ou invalido."}), 401

        return funcao(*args, usuario=dados, **kwargs)

    return wrapper