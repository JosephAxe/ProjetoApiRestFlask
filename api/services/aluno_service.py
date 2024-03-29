from ..models import aluno_model
from api import db


def cadastrar_aluno(aluno):
    aluno_bd = aluno_model.AlunoModel(nome=aluno.nome, data_nascimento=aluno.data_nascimento)
    db.session.add(aluno_bd)
    db.session.commit()
    return aluno_bd


def listar_alunos():
    alunos = aluno_model.AlunoModel.query.all()  # select * from aluno
    return alunos


def listar_alunos_id(identificador):
    aluno = aluno_model.AlunoModel.query.filter_by(id=identificador).first()  # select * from aluno
    return aluno


def atualizar_aluno(aluno_bd, aluno_atualizado):
    aluno_bd.nome = aluno_atualizado.nome
    aluno_bd.data_nascimento = aluno_atualizado.data_nascimento
    db.session.commit()


def excluir_aluno(aluno):
    db.session.delete(aluno)
    db.session.commit()



