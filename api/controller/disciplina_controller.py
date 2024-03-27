from flask_restful import Resource
from api import api
from ..schemas import disciplina_schema
from flask import request, make_response, jsonify
from ..dto import disciplina_dto
from ..services import disciplina_service


class DisciplinaController(Resource):
    @staticmethod
    def get():
        disciplinas = disciplina_service.listar_disciplinas()
        validate = disciplina_schema.DisciplinaSchema(many=True)
        return make_response(validate.jsonify(disciplinas), 200)

    @staticmethod
    def post():
        disciplinaSchema = disciplina_schema.DisciplinaSchema()
        validate = disciplinaSchema.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            novaDisciplina = disciplina_dto.DisciplinaDTO(nome=nome)
            retorno = disciplina_service.cadastrar_disciplina(novaDisciplina)
            disciplinaJson = disciplinaSchema.jsonify(retorno)
            return make_response(disciplinaJson, 201)

    @staticmethod
    def put(id):
        disciplina = disciplina_service.listar_disciplinas_id(id)
        if disciplina is None:
            return make_response(jsonify("Disciplina não encontrada!"), 404)
        disciplinaSchema = disciplina_schema.DisciplinaSchema()
        validate = disciplinaSchema.validate(request.json)
        if validate:
            make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            novaDisciplinaAlterada = disciplina_dto.DisciplinaDTO(nome)
            disciplina_service.atualizar_disciplina(disciplina, novaDisciplinaAlterada)
            disciplinaAtualizada = disciplina_service.listar_disciplinas_id(id)
            return make_response(disciplinaSchema.jsonify(disciplinaAtualizada), 200)

    @staticmethod
    def delete(id):
        disciplinaBD = disciplina_service.listar_disciplinas_id(id)
        if disciplinaBD is None:
            return make_response(jsonify("Disciplina não encontrada!"), 404)

        disciplina_service.excluir_disciplina(disciplinaBD)
        return make_response(jsonify("Disciplina excluido com sucesso!"), 204)


class DisciplinaDetailController(Resource):
    @staticmethod
    def get(id):
        disciplina = disciplina_service.listar_disciplinas_id(id)
        if disciplina is None:
            return make_response(jsonify("Disciplina não encontrada!"), 404)

        validate = disciplina_schema.DisciplinaSchema()
        return make_response(validate.jsonify(disciplina), 200)


api.add_resource(DisciplinaController, '/disciplina')
api.add_resource(DisciplinaController, '/disciplina/<int:id>', endpoint='alterar_excluir_disciplina', methods=["PUT","DELETE"])
api.add_resource(DisciplinaDetailController, '/disciplina/<int:id>')

