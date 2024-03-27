from ..models import curso_model
from api import db


def cadastrar_curso(curso):
    curso_bd = curso_model.CursoModel(nome=curso.nome, descricao=curso.descricao)
    db.session.add(curso_bd)
    db.session.commit()
    return curso_bd


def listar_cursos():
    cursos = curso_model.CursoModel.query.all()  # select * from curso
    return cursos


def listar_cursos_id(parametro_id):
    curso = curso_model.CursoModel.query.filter_by(id=parametro_id).first()  # select * from curso
    return curso


def atualizar_curso(curso_bd, curso_atualizado):
    curso_bd.nome = curso_atualizado.nome
    curso_bd.descricao = curso_atualizado.descricao
    db.session.commit()


def excluir_curso(curso):
    db.session.delete(curso)
    db.session.commit()