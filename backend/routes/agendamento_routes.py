from flask import Blueprint, jsonify, request
from services.agendamento_service import AgendamentoService
 
agendamento_bp = Blueprint("agendamentos", __name__)
service = AgendamentoService()
 
 
@agendamento_bp.route("/api/agendamentos", methods=["POST"])
def criar_agendamento():
    dados = request.get_json()
    try:
        agendamento = service.criar_agendamento(
            dados["cliente_id"], dados["profissional_id"],
            dados["servico_id"], dados["data_hora"],
        )
        return jsonify(vars(agendamento)), 201
    except (ValueError, KeyError) as erro:
        return jsonify({"erro": str(erro)}), 400
