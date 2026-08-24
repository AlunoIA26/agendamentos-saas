class Agendamento:
    def __init__(self, id, cliente_id, profissional_id, servico_id, data_hora, status="confirmado"):
        self.id = id
        self.cliente_id = cliente_id
        self.profissional_id = profissional_id
        self.servico_id = servico_id
        self.data_hora = data_hora
        self.status = status
