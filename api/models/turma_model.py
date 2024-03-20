from api import db


class TurmaModel(db.Model):
    __tablename__ = "turma"
    nome = db.Column(db.String(100), primary_key=True, autoincrement=True, nullable=False)
    descricao = db.Column(db.String(200), nullable=False)
    data_inicio = db.Column(db.Date, nullable=False)
    data_fim = db.Column(db.Date, nullable=False)