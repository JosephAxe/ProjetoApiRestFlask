from flask_restful import Resource
from api import api
from ..schemas import curso_schema
from flask import request, make_response, jsonify
from ..dto import curso_dto
from ..services import curso_service


class CursoController(Resource):
    @staticmethod
    def get():
        cursos = curso_service.listar_cursos()
        validate = curso_schema.CursoSchema(many=True)
        return make_response(validate.jsonify(cursos), 200)

    @staticmethod
    def post():
        cursoSchema = curso_schema.CursoSchema()
        validate = cursoSchema.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            descricao = request.json["descricao"]
            disciplinas = request.json["disciplinas"]

            novoCurso = curso_dto.CursoDTO(nome=nome, descricao=descricao, disciplinas=disciplinas)
            retorno = curso_service.cadastrar_curso(novoCurso)
            cursoJson = cursoSchema.jsonify(retorno)
            return make_response(cursoJson, 201)

    @staticmethod
    def put(id):
        curso = curso_service.listar_cursos_id(id)
        if curso is None:
            return make_response(jsonify("Curso não encontrado!"), 404)
        cursoSchema = curso_schema.CursoSchema()
        validate = cursoSchema.validate(request.json)
        if validate:
            make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            descricao = request.json["descricao"]
            disciplinas = request.json["disciplinas"]
            novoCursoAlterado = curso_dto.CursoDTO(nome, descricao, disciplinas=disciplinas)
            curso_service.atualizar_curso(curso, novoCursoAlterado)
            cursoAtualizada = curso_service.listar_cursos_id(id)
            return make_response(cursoSchema.jsonify(cursoAtualizada), 200)

    @staticmethod
    def delete(id):
        cursoBD = curso_service.listar_cursos_id(id)
        if cursoBD is None:
            return make_response(jsonify("Curso não encontrado!"), 404)

        curso_service.excluir_curso(cursoBD)
        return make_response(jsonify("Curso excluido com sucesso!"), 204)


class CursoDetailController(Resource):
    @staticmethod
    def get(id):
        curso = curso_service.listar_cursos_id(id)
        if curso is None:
            return make_response(jsonify("Curso não encontrado!"), 404)

        validate = curso_schema.CursoSchema()
        return make_response(validate.jsonify(curso), 200)


api.add_resource(CursoController, '/curso')
api.add_resource(CursoController, '/curso/<int:id>', endpoint='alterar_excluir_curso', methods=["PUT","DELETE"])
api.add_resource(CursoDetailController, '/curso/<int:id>')

