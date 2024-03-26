from api import ma
from ..models import disciplina_model
from marshmallow import fields


class DisciplinaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = disciplina_model.DisciplinaModel
        load_instance = True
        fields = ("id", "nome")

    id = fields.Integer(required=False)
    nome = fields.String(required=True)

