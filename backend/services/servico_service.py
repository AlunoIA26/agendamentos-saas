from repositories.servico_repository import ServicoRepository
from models.servico import Servico


class ServicoService:
    def __init__(self):
        self.repository = ServicoRepository()

    def adicionar_servico(self, nome, duracao_minutos, preco):
        if not nome or not nome.strip():
            raise ValueError("O nome do serviço é obrigatório.")

        try:
            duracao_minutos = int(duracao_minutos)
        except (TypeError, ValueError):
            raise ValueError("A duração deve ser um número inteiro.")

        if duracao_minutos <= 0:
            raise ValueError("A duração deve ser maior que zero.")

        try:
            preco = float(preco)
        except (TypeError, ValueError):
            raise ValueError("O preço deve ser um número.")

        if preco < 0:
            raise ValueError("O preço deve ser maior ou igual a zero.")

        servico = Servico(
            None,
            nome.strip(),
            duracao_minutos,
            preco,
        )

        return self.repository.adicionar(servico)

    def listar_servicos(self):
        return self.repository.listar_todos()