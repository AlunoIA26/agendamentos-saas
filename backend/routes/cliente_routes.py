from flask import Blueprint, jsonify, request
from services.cliente_service import ClienteService
 
cliente_bp = Blueprint("clientes", __name__)
service = ClienteService()
 
 
@cliente_bp.route("/api/clientes", methods=["GET"])
def listar_clientes():
    clientes = service.listar_clientes()
    return jsonify([vars(c) for c in clientes])
 
 
@cliente_bp.route("/api/clientes", methods=["POST"])
def criar_cliente():
    dados = request.get_json()
    try:
        cliente = service.adicionar_cliente(
            dados["nome"], dados.get("telefone"), dados["email"]
        )
        return jsonify(vars(cliente)), 201
    except (ValueError, KeyError) as erro:
        return jsonify({"erro": str(erro)}), 400
