from dataclasses import dataclass
 
 
@dataclass
class Profissional:
    id: int
    nome: str
    especialidade: str
 
    def __post_init__(self):
        if not self.nome or not self.nome.strip():
            raise ValueError("O nome do profissional não pode ser vazio.")
