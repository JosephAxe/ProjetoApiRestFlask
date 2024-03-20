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
            return make_response(jsonify(validate, 400))
        else:
            nome = request.json["nome"]
            data_nascimento = request.json["data_nascimento"]
            novoProfessor = professor_dto.ProfessorDTO(nome=nome, data_nascimento=data_nascimento)
            retorno = professor_service.cadastrar_professor(novoProfessor)
            professorJson = professorSchema.jsonify(retorno)
            return make_response(professorJson, 201)


api.add_resource(ProfessorController, '/professor')
