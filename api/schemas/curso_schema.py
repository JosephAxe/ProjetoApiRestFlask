from api import ma
from ..models import curso_model
from marshmallow import fields
from marshmallow_sqlalchemy import auto_field


class CursoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = curso_model.CursoModel
        load_instance = True
        fields = ("id", "nome", "descricao","disciplinas")

    # nome = fields.String(required=True)
    # descricao = fields.String(required=True)
    nome = auto_field()
    descricao = auto_field()
    disciplinas = auto_field()