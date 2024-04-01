from datetime import date
from dataclasses import dataclass

@dataclass
class TurmaDTO():
    nome: str
    descricao: str
    data_inicio: date
    data_fim: date
    curso_id: str
    