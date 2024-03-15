from flask_restful import Resource
from api import api
from ..schemas import aluno_schema
from flask import request, make_response, jsonify
from ..dto import aluno_dto
from ..services import aluno_service


class AlunoController(Resource):
    @staticmethod
    def get():
        return "Teste aluno"

    @staticmethod
    def post():
        alunoSchema = aluno_schema.AlunoSchema()
        validate = alunoSchema.validate(request.json)
        if validate:
            return make_response(jsonify(validate, 400))
        else:
            nome = request.json["nome"]
            data_nascimento = request.json["data_nascimento"]
            novoAluno = aluno_dto.AlunoDTO(nome=nome, data_nascimento=data_nascimento)
            retorno = aluno_service.cadastrar_aluno(novoAluno)
            alunoJson = alunoSchema.jsonify(retorno)
            return make_response(alunoJson, 201)


api.add_resource(AlunoController, '/aluno')
