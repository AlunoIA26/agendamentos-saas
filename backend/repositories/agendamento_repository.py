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