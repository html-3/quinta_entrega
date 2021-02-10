from flask import request, Blueprint, jsonify
from datetime import datetime
from app.extensions import db
from app.clientes.model import Cliente

clientes_api=Blueprint("clientes_api", __name__)

@clientes_api.route("/clientes", methods=["GET","POST"])
def marcar_servico():
    if request.method=="GET":
        clientes_todos=Clientes.query.all()
        return jsonify([cliente.json() for cliente in clientes_todos]),200

    if request.method=="POST":
        dados=request.json

        nome=dados.get("nome")
        nome_dono=dados.get("nome_dono")
        descricao=dados.get("descricao")
        endereco=dados.get("endereco")
        telefone=dados.get("telefone")
        horario_data=dados.get("horario_data")
        banho=dados.get("banho")
        tosa=dados.get("tosa")

        if nome==None or descricao==None or nome_dono==None or endereco==None or telefone==None or horario_data==None or (banho==False and tosa==False):
            return {"erro":"Há algum input vazio."},400

        if not isinstance(nome,str) or len(nome)>20 or not isinstance(nome_dono,str) or len(nome_dono)>50:
            return {"erro":"Nome inválido."},400
        if not isinstance(descricao,str) or len(descricao)>300:
            return {"erro":"Descricao inválida."},400
        if not isinstance(endereco,str) or len(endereco)>100:
            return {"erro":"Endereco inválido."},400
        if not isinstance(telefone,str) or len(telefone)>20:
            return {"erro":"Telefone inválido."},400
        try:
            datetime.datetime.strptime(horario_data, '%m/%d/%y %H:%M')
        except ValueError:
            return {"erro":"Horário e data inválidos."},400
        if not isinstance(banho,bool) or not isinstance(tosa,bool):
            return {"erro":"Servicos inválidos."},400

        cliente=Cliente(nome=nome,
                        descricao=descricao,
                        endereco=endereco,
                        telefone=telefone,
                        horario_data=horario_data,
                        banho=banho,
                        tosa=tosa)
        
        db.session.add(cliente)
        db.session.commit()

        return cliente.json(), 200

@clientes_api.route("/clientes/<int:id>",methods=["GET","PUT","PATCH","DELETE"])
def editar_servico(id):
    cliente=Cliente.query.get_or_404(id)
    
    if request.method=="GET":
        return cliente.json(),200

    if request.method=="PATCH":
        dados=request.json()

        nome=data.get("nome", cliente.nome)
        nome_dono=data.get("nome_dono")
        descricao=data.get("descricao", cliente.descricao)
        endereco=data.get("endereco", cliente.endereco)
        telefone=data.get("telefone", cliente.telefone)
        horario_data=data.get("horario_data", cliente.horario_data)
        banho=data.get("banho", cliente.banho)
        tosa=data.get("tosa", cliente.data)

        if nome==None or descricao==None or nome_dono==None or endereco==None or telefone==None or horario_data==None or (banho==False and tosa==False):
            return {"erro":"Há algum input vazio."},400

        if not isinstance(nome,str) or len(nome)>20 or not isinstance(nome_dono,str) or len(nome_dono)>50:
            return {"erro":"Nome inválido."},400
        if not isinstance(descricao,str) or len(descricao)>300:
            return {"erro":"Descricao inválida."},400
        if not isinstance(endereco,str) or len(endereco)>100:
            return {"erro":"Endereco inválido."},400
        if not isinstance(telefone,str) or len(telefone)>20:
            return {"erro":"Telefone inválido."},400
        if not isinstance(horario_data,datetime):
            return {"erro":"Horário e data inválidos."},400
        if not isinstance(banho,bool) or not isinstance(tosa,bool):
            return {"erro":"Servicos inválidos."},400

        cliente.nome=nome
        cliente.nome_dono=nome_dono
        cliente.descricao=descricao
        cliente.endereco=endereco
        cliente.telefone=telefone
        cliente.horario_data=horario_data
        cliente.banho=banho
        cliente.tosa=tosa

        db.session.commit()