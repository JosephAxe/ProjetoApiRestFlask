from ..models import turma_model
from api import db


def cadastrar_turma(turma):
    turma_bd = turma_model.TurmaModel(nome=turma.nome, descricao=turma.descricao, data_inicio=turma.data_inicio, data_fim=turma.data_fim)
    db.session.add(turma_bd)
    db.session.commit()
    return turma_bd


def listar_turmas():
    turmas = turma_model.TurmaModel.query.all()  # select * from turma
    return turmas


def listar_turmas_id(parametro_id):
    turma = turma_model.TurmaModel.query.filter_by(id=parametro_id).first()  # select * from turma
    return turma


def atualizar_turma(turma_bd, turma_atualizado):
    turma_bd.nome = turma_atualizado.nome
    turma_bd.descricao = turma_atualizado.descricao
    turma_bd.data_inicio = turma_atualizado.data_inicio
    turma_bd.data_fim = turma_atualizado.data_fim
    db.session.commit()


def excluir_turma(turma):
    db.session.delete(turma)
    db.session.commit()
