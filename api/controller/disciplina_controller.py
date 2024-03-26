from flask_restful import Resource
from api import api
from flask import request, make_response, jsonify
from ..services import disciplina_service
from ..schemas import disciplina_schema
from ..dto import disciplina_dto


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
            return make_response(jsonify(validate, 400))
        else:
            nome = request.json("nome")
            novaDisciplina = disciplina_dto.DisciplinaDTO(nome=nome)
            retorno = disciplina_service.cadastrar_disciplina(novaDisciplina)
            disciplinajson = disciplinaSchema.jsonify(retorno)
            return make_response(disciplinajson, 201)

    @staticmethod
    def put(id):
        disciplina = disciplina_service.listar_disciplinas_id()
        if disciplina is None:
            return make_response(jsonify("Disciplina não encontrada!"), 404)
        disciplinaSchema = disciplina_schema.DisciplinaSchema()
        validate = disciplinaSchema.validate(request.json)
        if validate:
            make_response(jsonify(validate), 400)
        else:
            nome = request.json("nome")
            novaDisciplinaalterada = disciplina_dto.DisciplinaDTO(nome)
            disciplina_service.atualizar_displina(disciplina, novaDisciplinaalterada)
            disciplinaAtualizada = disciplina_service.listar_disciplinas_id(id)
            return make_response(disciplinaSchema.jsonify(disciplinaAtualizada), 200)

    @staticmethod
    def delete(id):
        disciplinaBD = disciplina_service.listar_disciplina_id(id)
        if disciplinaBD is None:
            return make_response(jsonify("Turma não encontrada!"), 404)
        disciplina_service.exluir_disciplina(disciplinaBD)
        return make_response(jsonify("Turma excluida com sucesso"))

    class DisciplinaDetailController(Resource):
        @staticmethod
        def get(id):
            disciplina = disciplina_service.listar_disciplina_id(id)
            if disciplina is None:
                return make_response(jsonify("Turma não  encontrada!"))
            validate = disciplina_schema.DisciplinaSchema()
            return make_response(validate.jsonify(disciplina), 200)


api.add_resource(DisciplinaController, '/disciplina')
api.add_resource(DisciplinaController, '/disciplina/<int:id>', endpoint='alterar_excluir', methods=["PUT","DELETE"])
