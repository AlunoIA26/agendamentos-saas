from flask import Blueprint, jsonify, request

from services.agendamento_service import AgendamentoService
from routes.auth_routes import token_obrigatorio


agendamento_bp = Blueprint("agendamentos", __name__)
service = AgendamentoService()


def _serializar(agendamento):
    """Transforma um Agendamento em dicionario, com a data ISO."""
    dados = vars(agendamento).copy()

    if hasattr(dados.get("data_hora"), "isoformat"):
        dados["data_hora"] = dados["data_hora"].isoformat(
            timespec="minutes"
        )

    return dados


@agendamento_bp.route("/api/agendamentos", methods=["POST"])
def criar_agendamento():
    dados = request.get_json()

    try:
        agendamento = service.criar_agendamento(
            dados["cliente_id"],
            dados["profissional_id"],
            dados["servico_id"],
            dados["data_hora"],
        )

        return jsonify(_serializar(agendamento)), 201

    except (ValueError, KeyError) as erro:
        return jsonify({"erro": str(erro)}), 400


@agendamento_bp.route(
    "/api/agendamentos/<int:agendamento_id>/cancelar",
    methods=["POST"],
)
def cancelar(agendamento_id):
    try:
        service.cancelar_agendamento(agendamento_id)

        return jsonify({
            "mensagem": "Agendamento cancelado."
        })

    except ValueError as erro:
        return jsonify({"erro": str(erro)}), 400


@agendamento_bp.route(
    "/api/agendamentos",
    methods=["GET"],
)
@token_obrigatorio
def listar():
    agendamentos = service.listar_agendamentos()

    return jsonify([
        _serializar(a) for a in agendamentos
    ])


@agendamento_bp.route(
    "/api/clientes/<int:cliente_id>/historico",
    methods=["GET"],
)
def historico(cliente_id):
    agendamentos = service.historico_do_cliente(cliente_id)

    return jsonify([
        _serializar(a) for a in agendamentos
    ])


@agendamento_bp.route(
    "/api/agendamentos/<int:agendamento_id>/concluir",
    methods=["POST"],
)
def concluir(agendamento_id):
    try:
        service.concluir_agendamento(agendamento_id)

        return jsonify({
            "mensagem": "Agendamento concluído."
        })

    except ValueError as erro:
        return jsonify({"erro": str(erro)}), 400