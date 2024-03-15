from ..models import professor_model
from api import db


def cadastrar_professor(professor):
    professor_bd = professor_model.Aluno(nome=professor.nome, data_nascimento=professor.data_nascimento)
    db.session.add(professor_bd)
    db.session.commit()
    return professor_bd
