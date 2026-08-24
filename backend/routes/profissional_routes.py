from flask import Blueprint, jsonify, request
from services.profissional_service import ProfissionalService

profissional_bp = Blueprint("profissionais", __name__)
service = ProfissionalService()


@profissional_bp.route("/api/profissionais", methods=["GET"])
def listar_profissionais():
    profissionais = service.listar_profissionais()
    return jsonify([vars(p) for p in profissionais])


@profissional_bp.route("/api/profissionais", methods=["POST"])
def criar_profissional():
    dados = request.get_json()

    try:
        profissional = service.adicionar_profissional(
            dados["nome"],
            dados["especialidade"],
        )

        return jsonify(vars(profissional)), 201

    except (ValueError, KeyError) as erro:
        return jsonify({"erro": str(erro)}), 400