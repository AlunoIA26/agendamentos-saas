from repositories.profissional_repository import ProfissionalRepository
from models.profissional import Profissional


class ProfissionalService:
    def __init__(self):
        self.repository = ProfissionalRepository()

    def adicionar_profissional(self, nome, especialidade):
        if not nome or not nome.strip():
            raise ValueError("O nome do profissional é obrigatório.")

        if not especialidade or not especialidade.strip():
            raise ValueError("A especialidade do profissional é obrigatória.")

        profissional_existente = self.repository.buscar_por_nome(nome.strip())

        if profissional_existente:
            raise ValueError(
                "Já existe um profissional cadastrado com esse nome."
            )

        profissional = Profissional(
            None,
            nome.strip(),
            especialidade.strip(),
        )

        return self.repository.adicionar(profissional)

    def listar_profissionais(self):
        return self.repository.listar_todos()