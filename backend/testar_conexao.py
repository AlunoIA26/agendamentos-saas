from repositories.cliente_repository import ClienteRepository
from models.cliente import Cliente
 
repo = ClienteRepository()
repo.adicionar(Cliente(None, "Maria Silva", "11999990000", "maria@email.com"))
 
for cliente in repo.listar_todos():
    print(cliente.nome, cliente.telefone, cliente.email)
