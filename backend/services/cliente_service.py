from repositories.cliente_repository import ClienteRepository
from models.cliente import Cliente
 
 
class ClienteService:
    def __init__(self):
        self.repository = ClienteRepository()
 
    def adicionar_cliente(self, nome, telefone, email):
        cliente = Cliente(None, nome, telefone, email)
        return self.repository.adicionar(cliente)
 
    def listar_clientes(self):
        return self.repository.listar_todos()

    def remover_cliente(self, cliente_id):
        from repositories.agendamento_repository import AgendamentoRepository
        agendamentos = AgendamentoRepository()
        if agendamentos.existe_agendamento_para_cliente(cliente_id):
            raise ValueError("Não é possível excluir um cliente com agendamentos.")
        self.repository.remover(cliente_id)

