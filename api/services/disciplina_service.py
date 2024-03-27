from ..models import disciplina_model
from api import db


def cadastrar_disciplina(disciplina):
    disciplina_bd = disciplina_model.DisciplinaModel(nome=disciplina.nome)
    db.session.add(disciplina_bd)
    db.session.commit()
    return disciplina_bd


def listar_disciplinas():
    disciplinas = disciplina_model.DisciplinaModel.query.all()  # select * from disciplina
    return disciplinas


def listar_disciplinas_id(parametro_id):
    disciplina = disciplina_model.DisciplinaModel.query.filter_by(id=parametro_id).first()  # select * from disciplina
    return disciplina


def atualizar_disciplina(disciplina_bd, disciplina_atualizado):
    disciplina_bd.nome = disciplina_atualizado.nome
    db.session.commit()


def excluir_disciplina(disciplina):
    db.session.delete(disciplina)
    db.session.commit()