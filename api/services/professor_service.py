from ..models import professor_model
from api import db


def cadastrar_professor(professor):
    professor_bd = professor_model.Professor(nome=professor.nome, data_nascimento=professor.data_nascimento)
    db.session.add(professor_bd)
    db.session.commit()
    return professor_bd


def listar_professores():
    professores = professor_model.Professor.query.all() # select * from aluno
    return professores


