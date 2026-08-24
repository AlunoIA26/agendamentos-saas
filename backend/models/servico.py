from dataclasses import dataclass


@dataclass
class Servico:
    id: int
    nome: str
    duracao_minutos: int
    preco: float