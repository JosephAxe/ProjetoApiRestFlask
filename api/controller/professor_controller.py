from flask_restful import Resource
from api import api
from ..schemas import professor_schema
from flask import request, make_response, jsonify
from ..dto import professor_dto
from ..services import professor_service


class ProfessorController(Resource):
    @staticmethod
    def get():
        professor = professor_service.listar_professores()
        validate = professor_schema.ProfessorSchema(many=True)
        return make_response(validate.jsonify(professor), 200)

    @staticmethod
    def post():
        professorSchema = professor_schema.ProfessorSchema()
        validate = professorSchema.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            data_nascimento = request.json["data_nascimento"]
            novoProfessor = professor_dto.ProfessorDTO(nome=nome, data_nascimento=data_nascimento)
            retorno = professor_service.cadastrar_professor(novoProfessor)
            professorJson = professorSchema.jsonify(retorno)
            return make_response(professorJson, 201)

    @staticmethod
    def put(id):
        professor = professor_service.listar_professores_id(id)
        if professor is None:
            return make_response(jsonify("Professor não encontrado!"), 404)
        professorSchema = professor_schema.ProfessorSchema()
        validate = professorSchema.validate(request.json)
        if validate:
            make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            data_nascimento = request.json["data_nascimento"]
            novoProfessorAlterado = professor_dto.ProfessorDTO(nome, data_nascimento)
            professor_service.atualizar_professor(professor, novoProfessorAlterado)
            professorAtualizado = professor_service.listar_professores_id(id)
            return make_response(professorSchema.jsonify(professorAtualizado), 200)


    @staticmethod
    def delete(id):
        professorBD = professor_service.listar_professores_id(id)
        if professorBD is None:
            return make_response(jsonify("Professor não encontrado!"), 404)
        professor_service.excluir_professor(professorBD)
        return make_response(jsonify("Professor excluido com sucesso!"), 204)


class ProfessorDetailController(Resource):
    @staticmethod
    def get(id):
        professor = professor_service.listar_professores_id(id)
        if professor is None:
            return make_response(jsonify("Professor não encontrado!"), 404)
        validate = professor_schema.ProfessorSchema()
        return make_response(validate.jsonify(professor), 200)


api.add_resource(ProfessorController, '/professor')
api.add_resource(ProfessorController, '/professor/<int:id>', endpoint='alterar_excluir_professor', methods=["PUT","DELETE"])
api.add_resource(ProfessorDetailController, '/professor/<int:id>')

