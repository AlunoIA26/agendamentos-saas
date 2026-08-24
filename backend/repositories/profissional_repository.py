from config.database import conectar
from models.profissional import Profissional


class ProfissionalRepository:
    def adicionar(self, profissional):
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            """
            INSERT INTO profissionais (nome, especialidade)
            VALUES (%s, %s)
            RETURNING id
            """,
            (profissional.nome, profissional.especialidade),
        )

        novo_id = cursor.fetchone()[0]

        conexao.commit()
        cursor.close()
        conexao.close()

        profissional.id = novo_id
        return profissional

    def listar_todos(self):
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            "SELECT id, nome, especialidade FROM profissionais"
        )

        linhas = cursor.fetchall()

        cursor.close()
        conexao.close()

        return [Profissional(*linha) for linha in linhas]

    def buscar_por_nome(self, nome):
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            "SELECT id, nome, especialidade FROM profissionais WHERE nome = %s",
            (nome,),
        )

        linha = cursor.fetchone()

        cursor.close()
        conexao.close()

        if linha:
            return Profissional(*linha)

        return None

    def remover(self, profissional_id):
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            "DELETE FROM profissionais WHERE id = %s",
            (profissional_id,),
        )

        conexao.commit()
        cursor.close()
        conexao.close()