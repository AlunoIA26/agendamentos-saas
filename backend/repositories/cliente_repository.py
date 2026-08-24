from config.database import conectar
from models.cliente import Cliente
 
 
class ClienteRepository:
    def adicionar(self, cliente):
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute(
            "INSERT INTO clientes (nome, telefone, email) VALUES (%s, %s, %s) RETURNING id",
            (cliente.nome, cliente.telefone, cliente.email),
        )
        novo_id = cursor.fetchone()[0]
        conexao.commit()
        cursor.close()
        conexao.close()
        cliente.id = novo_id
        return cliente
 
    def listar_todos(self):
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT id, nome, telefone, email FROM clientes")
        linhas = cursor.fetchall()
        cursor.close()
        conexao.close()
        return [Cliente(*linha) for linha in linhas]
 
    def remover(self, cliente_id):
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM clientes WHERE id = %s", (cliente_id,))
        conexao.commit()
        cursor.close()
        conexao.close()
