from dataclasses import dataclass


@dataclass
class CursoDTO():
    nome: str
    descricao: str
    disciplinas: list
