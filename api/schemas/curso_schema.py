from api import ma
from ..models import curso_model
from marshmallow import fields


class CursoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = curso_model.CursoModel
        load_instance = True
        fields = ("id", "nome", "descricao")

    nome = fields.String(required=True)
    descricao = fields.String(required=True)
