from dataclasses import dataclass
 
 
@dataclass
class Servico:
    id: int
    nome: str
    duracao_minutos: int
    preco: float
 
    def __post_init__(self):
        if self.duracao_minutos <= 0:
            raise ValueError("A duração do serviço precisa ser maior que zero.")
        if self.preco < 0:
            raise ValueError("O preço não pode ser negativo.")
