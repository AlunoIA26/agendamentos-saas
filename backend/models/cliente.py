import re
from dataclasses import dataclass
 
 
@dataclass
class Cliente:
    id: int
    nome: str
    telefone: str
    email: str
 
    def __post_init__(self):
        if not self.nome or not self.nome.strip():
            raise ValueError("O nome do cliente não pode ser vazio.")
        if not re.match(r"^[^@]+@[^@]+\.[^@]+$", self.email):
            raise ValueError(f"E-mail inválido: {self.email}")
