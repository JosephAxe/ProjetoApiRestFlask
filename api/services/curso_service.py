from ..models import curso_model
from api import db
from .disciplina_service import listar_disciplinas_id


def cadastrar_curso(curso):
    curso_bd = curso_model.CursoModel(nome=curso.nome, descricao=curso.descricao)
    for i in curso.disciplinas:
        disciplina = listar_disciplinas_id(i)
        curso_bd.disciplinas.append(disciplina)
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
    curso_bd.disciplinas = []
    for i in curso_atualizado.disciplinas:
        disciplina = listar_disciplinas_id(i)
        curso_bd.disciplinas.append(disciplina)

    db.session.commit()


def excluir_curso(curso):
    db.session.delete(curso)
    db.session.commit()