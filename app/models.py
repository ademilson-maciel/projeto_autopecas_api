from app.database import db

class Peca(db.Model):
    id_codigo = db.Column(db.String(20), primary_key=True)
    descricao = db.Column(db.String(100), nullable=False)
    fabricante = db.Column(db.String(50), nullable=False)
    aplicacao = db.Column(db.String(100), nullable=False)