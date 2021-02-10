
from app.extensions import db

class Cliente(db.Model):
    __tablename__="clientes"
    id=db.Column(db.Integer,primary_key=True)
    nome=db.Column(db.String(20),nullable=False)
    nome_dono=db.Column(db.String(50),nullable=False)
    descricao=db.Column(db.String(300),nullable=False)
    endereco=db.Column(db.String(100),nullable=False)
    telefone=db.Column(db.String(20),nullable=False)
    horario=db.Column(db.String(5),nullable=False)
    banho=db.Column(db.Boolean,nullable=False)
    tosa=db.Column(db.Boolean,nullable=False)

    def json(self):
        return{
            "nome": self.nome,
            "nome_dono": self.nome_dono,
            "descricao": self.descricao,
            "endereco": self.endereco,
            "telefone": self.telefone,
            "horario": self.horario,
            "banho": self.banho,
            "tosa": self.tosa
        }


