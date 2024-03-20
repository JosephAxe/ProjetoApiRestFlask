from flask_restful import Resource
from api import api
from ..schemas import aluno_schema
from flask import request, make_response, jsonify
from ..dto import aluno_dto
from ..services import aluno_service


class AlunoController(Resource):
    @staticmethod
    def get():
        alunos = aluno_service.listar_alunos()
        validate = aluno_schema.AlunoSchema(many=True)
        return make_response(validate.jsonify(alunos), 200)

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

    @staticmethod
    def put(id):
        aluno = aluno_service.listar_alunos_id(id)
        if aluno is None:
            return make_response(jsonify("Aluno não encontrado!"), 404)
        alunoSchema = aluno_schema.AlunoSchema()
        validate = alunoSchema.validate(request.json)
        if validate:
            make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            data_nascimento = request.json["data_nascimento"]
            novoAlunoAlterado = aluno_dto.AlunoDTO(nome, data_nascimento)
            aluno_service.atualizar_aluno(aluno, novoAlunoAlterado)
            alunoAtualizado = aluno_service.listar_alunos_id(id)
            return make_response(alunoSchema.jsonify(alunoAtualizado),200)

    @staticmethod
    def delete(id):
        alunoBD = aluno_service.listar_alunos_id(id)
        if alunoBD is None:
            return make_response(jsonify("Aluno não encontrado!"), 404)

        aluno_service.excluir_aluno(alunoBD)
        return make_response(jsonify("Aluno excluido com sucesso!"),204)



class AlunoDetailController(Resource):
    @staticmethod
    def get(id):
        aluno = aluno_service.listar_alunos_id(id)
        if aluno is None:
            return make_response(jsonify("Aluno não encontrado"), 404)

        validate = aluno_schema.AlunoSchema()
        return make_response(validate.jsonify(aluno), 200)


api.add_resource(AlunoController, '/aluno')
api.add_resource(AlunoController, '/aluno/<int:id>', endpoint='alterar', methods=["PUT"])
api.add_resource(AlunoController, '/aluno/<int:id>', endpoint='excluir', methods=["DELETE"])
api.add_resource(AlunoDetailController, '/aluno/<int:id>')
