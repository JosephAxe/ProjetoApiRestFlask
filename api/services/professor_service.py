from ..models import professor_model
from api import db


def cadastrar_professor(professor):
    professor_bd = professor_model.ProfessorModel(nome=professor.nome, data_nascimento=professor.data_nascimento)
    db.session.add(professor_bd)
    db.session.commit()
    return professor_bd


def listar_professores():
    professores = professor_model.ProfessorModel.query.all() # select * from aluno
    return professores


def listar_professores_id(parametro_id):
    professor = professor_model.ProfessorModel.query.filter_by(id=parametro_id).first()  # select * from professor
    return professor


def atualizar_professor(professor_bd, professor_atualizado):
    professor_bd.nome = professor_atualizado.nome
    professor_bd.data_nascimento = professor_atualizado.data_nascimento
    db.session.commit()


def excluir_professor(professor):
    db.session.delete(professor)
    db.session.commit()