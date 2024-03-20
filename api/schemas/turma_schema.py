from api import ma
from ..models import turma_model
from marshmallow import fields


class TurmaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = turma_model.TurmaModel
        load_instance = True
        fields = ("nome", "descricao", "data_inicio", "data_fim")

    nome = fields.String(required=True)
    descricao = fields.Date(required=True)
    data_inicio = fields.Date(required=True)
    data_fim = fields.Date(required=True)
