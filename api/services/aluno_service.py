from ..models import aluno_model
from api import db


def cadastrar_aluno(aluno):
    aluno_bd = aluno_model.Aluno(nome=aluno.nome, data_nascimento=aluno.data_nascimento)
    db.session.add(aluno_bd)
    db.session.commit()
    return aluno_bd
