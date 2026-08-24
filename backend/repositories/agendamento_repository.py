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
