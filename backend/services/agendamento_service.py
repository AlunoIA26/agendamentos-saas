from repositories.agendamento_repository import AgendamentoRepository
from repositories.cliente_repository import ClienteRepository
from repositories.profissional_repository import ProfissionalRepository
from repositories.servico_repository import ServicoRepository
from models.agendamento import Agendamento
 
 
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
        ids_profissionais = [p.id for p in self.profissionais.listar_todos()]
        if profissional_id not in ids_profissionais:
            raise ValueError("Profissional não encontrado.")
 
        conflitos = self.repository.listar_por_profissional_e_data(
            profissional_id, data_hora
        )
        if conflitos:
            raise ValueError("Já existe um agendamento para este profissional neste horário.")
 
        agendamento = Agendamento(None, cliente_id, profissional_id, servico_id, data_hora)
        return self.repository.adicionar(agendamento)
