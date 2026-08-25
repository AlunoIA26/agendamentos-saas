import csv
import io

from flask import Blueprint, Response, jsonify, request

from services.agendamento_service import AgendamentoService
from routes.auth_routes import token_obrigatorio


relatorio_bp = Blueprint("relatorios", __name__)
service = AgendamentoService()


def _periodo():
    """Le inicio e fim da query string (?inicio=AAAA-MM-DD&fim=AAAA-MM-DD)."""
    inicio = request.args.get("inicio") or None
    fim = request.args.get("fim") or None

    return inicio, fim


@relatorio_bp.route(
    "/api/relatorios/faturamento",
    methods=["GET"],
)
@token_obrigatorio
def faturamento():
    inicio, fim = _periodo()

    return jsonify(
        service.relatorio_faturamento(inicio, fim)
    )


@relatorio_bp.route(
    "/api/relatorios/faturamento/csv",
    methods=["GET"],
)
def faturamento_csv():
    inicio, fim = _periodo()

    dados = service.relatorio_faturamento(inicio, fim)

    saida = io.StringIO()

    # O Excel em portugues espera ponto-e-virgula como
    # separador de colunas.
    escritor = csv.writer(saida, delimiter=";")

    escritor.writerow([
        "Profissional",
        "Atendimentos",
        "Faturamento",
    ])

    for linha in dados:
        # E virgula como separador decimal.
        valor = f"{linha['faturamento']:.2f}".replace(".", ",")

        escritor.writerow([
            linha["profissional"],
            linha["atendimentos"],
            valor,
        ])

    # O BOM (\ufeff) no inicio do arquivo avisa o
    # Excel que o texto e UTF-8.
    # Sem ele, nomes com acento aparecem embaralhados.
    conteudo = "\ufeff" + saida.getvalue()

    nome = "faturamento.csv"

    if inicio or fim:
        nome = (
            f"faturamento_{inicio or 'inicio'}"
            f"_a_{fim or 'hoje'}.csv"
        )

    return Response(
        conteudo,
        mimetype="text/csv",
        headers={
            "Content-Disposition": f"attachment; filename={nome}"
        },
    )