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
