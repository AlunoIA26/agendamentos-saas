from repositories.agendamento_repository import AgendamentoRepository
from repositories.cliente_repository import ClienteRepository
from repositories.profissional_repository import ProfissionalRepository
from repositories.servico_repository import ServicoRepository
from models.agendamento import Agendamento
from datetime import datetime, timedelta

def _iso(valor):
    """Converte data/hora para o formato ISO (2026-07-30T10:00).
 
    Sem esta conversao, o Flask serializa a data no formato
    HTTP ("Thu, 30 Jul 2026 10:00:00 GMT"), que o JavaScript
    interpreta como UTC e exibe com o fuso trocado.
    """
    if hasattr(valor, "isoformat"):
        return valor.isoformat(timespec="minutes")
    return valor

 
class AgendamentoService:
    def __init__(self):
        self.repository = AgendamentoRepository()
        self.clientes = ClienteRepository()
        self.profissionais = ProfissionalRepository()
        self.servicos = ServicoRepository()
 
    def criar_agendamento(self, cliente_id, profissional_id, servico_id, data_hora):
        ids_clientes = [c.id for c in self.clientes.listar_todos()]
        if cliente_id not in ids_clientes:
            raise ValueError("Cliente não encontrado.")
 
        servico = next(
            (s for s in self.servicos.listar_todos() if s.id == servico_id), None
        )
        if servico is None:
            raise ValueError("Serviço não encontrado.")
 
        inicio = datetime.fromisoformat(data_hora)
        fim = inicio + timedelta(minutes=servico.duracao_minutos)
 
        conflitos = self.repository.listar_conflitos(
            profissional_id, inicio.isoformat(), fim.isoformat()
        )
        if conflitos:
            raise ValueError("Este horário conflita com outro agendamento do profissional.")
 
        agendamento = Agendamento(None, cliente_id, profissional_id, servico_id, data_hora)
        return self.repository.adicionar(agendamento)

    def proximos_agendamentos(self, profissional_id, minutos=15):
            agora = datetime.now()
            limite = agora + timedelta(minutes=minutos)
            return self.repository.listar_por_profissional_e_periodo(
                profissional_id, agora.isoformat(), limite.isoformat()
            )

    def cancelar_agendamento(self, agendamento_id):
        agendamento = self.repository.buscar_por_id(agendamento_id)
        if agendamento is None:
            raise ValueError("Agendamento não encontrado.")
        if agendamento.status == "concluido":
            raise ValueError("Não é possível cancelar um agendamento já concluído.")
        self.repository.atualizar_status(agendamento_id, "cancelado")
 
    def concluir_agendamento(self, agendamento_id):
        agendamento = self.repository.buscar_por_id(agendamento_id)
        if agendamento is None:
            raise ValueError("Agendamento não encontrado.")
        self.repository.atualizar_status(agendamento_id, "concluido")
 
    def historico_do_cliente(self, cliente_id):
        return self.repository.historico_do_cliente(cliente_id)

    def listar_agendamentos(self):
        linhas = self.repository.listar_todos_detalhado()
        return [
            {
                "id": id_,
                "cliente": cliente,
                "profissional": profissional,
                "servico": servico,
                "data_hora": _iso(data_hora),
                "status": status,
            }
            for id_, cliente, profissional, servico,
                data_hora, status in linhas
        ]

    def relatorio_faturamento(self, inicio=None, fim=None):
        linhas = self.repository.faturamento_por_profissional(
            inicio, fim
        )

        return [
            {
                "profissional_id": profissional_id,
                "profissional": nome,
                "atendimentos": total,
                "faturamento": float(faturamento),
            }
            for profissional_id, nome, total, faturamento in linhas
        ]


