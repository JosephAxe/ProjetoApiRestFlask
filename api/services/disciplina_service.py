from ..models import disciplina_model
from api import db


def cadastrar_disciplina(disciplina):
    disciplina_bd = disciplina_model.DisciplinaModel(nome=disciplina.nome)
    db.session.add(disciplina_bd)
    db.session.commit()
    return disciplina_bd


def listar_disciplinas():
    disciplina = disciplina_model.DisciplinaModel().query.all()
    return disciplina


def listar_disciplina_id(parametro_id):
    disciplina = disciplina_model.DisciplinaModel.query.filter_by(id=parametro_id).first()


def atualizar_displina(disciplina_bd, disciplina_atualizada):
    disciplina_bd.nome = disciplina_atualizada.nome
    db.session.commit()


def exluir_disciplina(disciplina):
    db.session.delete(disciplina)
    db.session.commit()
