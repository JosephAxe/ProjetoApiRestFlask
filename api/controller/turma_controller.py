from flask_restful import Resource
from api import api
from ..schemas import turma_schema
from flask import request, make_response, jsonify
from ..dto import turma_dto
from ..services import turma_service


class TurmaController(Resource):
    @staticmethod
    def get():
        turmas = turma_service.listar_turmas()
        validate = turma_schema.TurmaSchema(many=True)
        return make_response(validate.jsonify(turmas), 200)

    @staticmethod
    def post():
        turmaSchema = turma_schema.TurmaSchema()
        validate = turmaSchema.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            descricao = request.json["descricao"]
            data_inicio = request.json["data_inicio"]
            data_fim = request.json["data_fim"]
            novaTurma = turma_dto.TurmaDTO(nome=nome, descricao=descricao, data_inicio=data_inicio, data_fim=data_fim)
            retorno = turma_service.cadastrar_turma(novaTurma)
            turmaJson = turmaSchema.jsonify(retorno)
            return make_response(turmaJson, 201)

    @staticmethod
    def put(id):
        turma = turma_service.listar_turmas_id(id)
        if turma is None:
            return make_response(jsonify("Turma não encontrado!"), 404)
        turmaSchema = turma_schema.TurmaSchema()
        validate = turmaSchema.validate(request.json)
        if validate:
            make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            descricao = request.json["descricao"]
            data_inicio = request.json["data_inicio"]
            data_fim = request.json["data_fim"]
            novaTurmaAlterado = turma_dto.TurmaDTO(nome,descricao, data_inicio, data_fim)
            turma_service.atualizar_turma(turma, novaTurmaAlterado)
            turmaAtualizada = turma_service.listar_turmas_id(id)
            return make_response(turmaSchema.jsonify(turmaAtualizada), 200)

    @staticmethod
    def delete(id):
        turmaBD = turma_service.listar_turmas_id(id)
        if turmaBD is None:
            return make_response(jsonify("Turma não encontrado!"), 404)

        turma_service.excluir_turma(turmaBD)
        return make_response(jsonify("Turma excluido com sucesso!"),204)


class TurmaDetailController(Resource):
    @staticmethod
    def get(id):
        turma = turma_service.listar_turmas_id(id)
        if turma is None:
            return make_response(jsonify("Turma não encontrado!"), 404)

        validate = turma_schema.TurmaSchema()
        return make_response(validate.jsonify(turma), 200)


api.add_resource(TurmaController, '/turma')
api.add_resource(TurmaController, '/turma/<int:id>', endpoint='alterar_excluir_turma', methods=["PUT","DELETE"])
api.add_resource(TurmaDetailController, '/turma/<int:id>')

