
from app.extensions import db

class Cliente(db.Model):
    __tablename__="clientes"
    id=db.Column(db.Integer,primary_key=True)
    nome=db.Column(db.String(20),nullable=False)
    descricao=db.Column(db.String(300),nullable=False)
    endereco=db.Column(db.String(100),nullable=False)
    contato=db.Column(db.String(20),nullable=False)
    horario_dia=db.Column(db.DateTime,nullable=False)
    banho=db.Column(db.Boolean,default=False)
    tosa=db.Column(db.Boolean,default=False)
