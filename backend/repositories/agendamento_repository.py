from config.database import conectar
from models.agendamento import Agendamento


class AgendamentoRepository:

    def adicionar(self, agendamento):
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            """INSERT INTO agendamentos
               (cliente_id, profissional_id, servico_id, data_hora, status)
               VALUES (%s, %s, %s, %s, %s) RETURNING id""",
            (
                agendamento.cliente_id,
                agendamento.profissional_id,
                agendamento.servico_id,
                agendamento.data_hora,
                agendamento.status,
            ),
        )

    

        novo_id = cursor.fetchone()[0]

        conexao.commit()
        cursor.close()
        conexao.close()

        agendamento.id = novo_id
        return agendamento

    def listar_conflitos(self, profissional_id, inicio, fim):
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute(
            """SELECT a.id, a.cliente_id, a.profissional_id, a.servico_id,
                      a.data_hora, a.status
               FROM agendamentos a
               JOIN servicos s ON s.id = a.servico_id
               WHERE a.profissional_id = %s
                 AND a.status != 'cancelado'
                 AND a.data_hora < %s
                 AND a.data_hora + (s.duracao_minutos * INTERVAL '1 minute') > %s""",
            (profissional_id, fim, inicio),
        )
        linhas = cursor.fetchall()
        cursor.close()
        conexao.close()
        return [Agendamento(*linha) for linha in linhas]
 
    def listar_por_profissional_e_periodo(self, profissional_id, inicio, fim):
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute(
            """SELECT id, cliente_id, profissional_id, servico_id, data_hora, status
               FROM agendamentos
               WHERE profissional_id = %s AND status != 'cancelado'
               AND data_hora < %s AND data_hora >= %s""",
            (profissional_id, fim, inicio),
        )
        linhas = cursor.fetchall()
        cursor.close()
        conexao.close()
        return [Agendamento(*linha) for linha in linhas]

    def buscar_por_id(self, agendamento_id):
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute(
            """SELECT id, cliente_id, profissional_id, servico_id, data_hora, status
               FROM agendamentos WHERE id = %s""",
            (agendamento_id,),
        )
        linha = cursor.fetchone()
        cursor.close()
        conexao.close()
        return Agendamento(*linha) if linha else None
 
    def atualizar_status(self, agendamento_id, novo_status):
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute(
            "UPDATE agendamentos SET status = %s WHERE id = %s",
            (novo_status, agendamento_id),
        )
        conexao.commit()
        cursor.close()
        conexao.close()
 
    def historico_do_cliente(self, cliente_id):
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute(
            """SELECT id, cliente_id, profissional_id, servico_id, data_hora, status
               FROM agendamentos WHERE cliente_id = %s ORDER BY data_hora""",
            (cliente_id,),
        )
        linhas = cursor.fetchall()
        cursor.close()
        conexao.close()
        return [Agendamento(*linha) for linha in linhas]

    def listar_todos_detalhado(self):
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute(
            """SELECT a.id, c.nome, p.nome, s.nome, a.data_hora, a.status
               FROM agendamentos a
               JOIN clientes c ON c.id = a.cliente_id
               JOIN profissionais p ON p.id = a.profissional_id
               JOIN servicos s ON s.id = a.servico_id
               ORDER BY a.data_hora"""
        )
        linhas = cursor.fetchall()
        cursor.close()
        conexao.close()
        return linhas

    def faturamento_por_profissional(self, inicio=None, fim=None):
        conexao = conectar()
        cursor = conexao.cursor()

        sql = """
            SELECT
                p.id,
                p.nome,
                COUNT(a.id),
                COALESCE(SUM(s.preco), 0)
            FROM agendamentos a
            JOIN profissionais p ON p.id = a.profissional_id
            JOIN servicos s ON s.id = a.servico_id
            WHERE a.status = 'concluido'
        """

        params = []

        if inicio:
            sql += " AND a.data_hora >= %s"
            params.append(inicio)

        if fim:
            sql += " AND a.data_hora < (%s::date + INTERVAL '1 day')"
            params.append(fim)

        sql += " GROUP BY p.id, p.nome ORDER BY p.nome"

        cursor.execute(sql, tuple(params))

        linhas = cursor.fetchall()

        cursor.close()
        conexao.close()

        return linhas

