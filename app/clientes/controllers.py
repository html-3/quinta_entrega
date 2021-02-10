from flask import request, Blueprint, jsonify
from app.extensions import db
from app.clientes.model import Cliente

clientes_api=Blueprint("clientes_api", __name__)

@clientes_api.route("/clientes", methods=["GET","POST"])
def marcar_servico():
    if request.method=="GET":
        clientes_todos=Cliente.query.all()
        return jsonify([cliente.json() for cliente in clientes_todos]),200

    if request.method=="POST":
        dados=request.json

        nome=dados.get("nome")
        nome_dono=dados.get("nome_dono")
        descricao=dados.get("descricao")
        endereco=dados.get("endereco")
        telefone=dados.get("telefone")
        horario=dados.get("horario")
        banho=dados.get("banho")
        tosa=dados.get("tosa")

        #comandos para validar atributos, nao está funcionando com "".
        if nome is None or descricao is None or nome_dono is None or endereco is None or telefone is None or horario is None or banho is None or tosa is None:
            return {"erro":"Há algum input vazio."},400

        if not isinstance(nome,str) or len(nome)>20:
            return {"erro":"Nome inválido."},400
        if not isinstance(nome_dono,str) or len(nome_dono)>50:
            return {"erro":"Nome do cliente inválido."},400
        if not isinstance(descricao,str) or len(descricao)>300:
            return {"erro":"Descricao inválida."},400
        if not isinstance(endereco,str) or len(endereco)>100:
            return {"erro":"Endereco inválido."},400
        if not isinstance(telefone,str) or len(telefone)>20:
            return {"erro":"Telefone inválido."},400
        #dado do tipo datetime estava muito difícil de comprender em tao pouco tempo.
        if not isinstance(horario,str) or ("9:00","10:00","11:00","13:00","14:00","15:00","16:00","17:00").count(horario)==0:
            return {"erro":"Horário inválido."},400
        if not isinstance(banho,bool) or not isinstance(tosa,bool):
            return {"erro":"Servicos inválidos."},400

        cliente=Cliente(nome=nome,
                        nome_dono=nome_dono,
                        descricao=descricao,
                        endereco=endereco,
                        telefone=telefone,
                        horario=horario,
                        banho=banho,
                        tosa=tosa)
        
        db.session.add(cliente)
        db.session.commit()

        return cliente.json(), 200

@clientes_api.route("/clientes/<int:id>",methods=["GET","PATCH","DELETE"])
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
        horario=data.get("horario", cliente.horario)
        banho=data.get("banho", cliente.banho)
        tosa=data.get("tosa", cliente.data)

        #comandos para validar atributos, nao está funcionando com "".
        if nome is None or descricao is None or nome_dono is None or endereco is None or telefone is None or horario is None or banho is None or tosa is None:
            return {"erro":"Há algum input vazio."},400

        if not isinstance(nome,str) or len(nome)>20:
            return {"erro":"Nome inválido."},400
        if not isinstance(nome_dono,str) or len(nome_dono)>50:
            return {"erro":"Nome do cliente inválido."},400
        if not isinstance(descricao,str) or len(descricao)>300:
            return {"erro":"Descricao inválida."},400
        if not isinstance(endereco,str) or len(endereco)>100:
            return {"erro":"Endereco inválido."},400
        if not isinstance(telefone,str) or len(telefone)>20:
            return {"erro":"Telefone inválido."},400
        #dado do tipo datetime estava muito difícil de comprender em tao pouco tempo.
        if not isinstance(horario,str) or ("9:00","10:00","11:00","13:00","14:00","15:00","16:00","17:00").count(horario)==0:
            return {"erro":"Horário inválido."},400
        if not isinstance(banho,bool) or not isinstance(tosa,bool):
            return {"erro":"Servicos inválidos."},400

        cliente.nome=nome
        cliente.nome_dono=nome_dono
        cliente.descricao=descricao
        cliente.endereco=endereco
        cliente.telefone=telefone
        cliente.horario=horario
        cliente.banho=banho
        cliente.tosa=tosa
        
        db.session.commit()

    if request.method=="DELETE": #incompleto, nao funciona
        db.session.remove(id)
        
        db.session.commit()