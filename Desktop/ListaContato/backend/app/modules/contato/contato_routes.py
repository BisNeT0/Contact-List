from flask import Blueprint, jsonify, request
from app.modules.contato.contato_dao import ContatoDAO

contato_routes = Blueprint("contato",__name__)
contato_dao = ContatoDAO()

@contato_routes.route("/api/v1/contato", methods=["POST"])
def salvar():
    print("Metodo Salvar foi invocado")
    if request.json:
        if 'nome' in request.json \
        and 'email' in request.json \
        and 'telefone' in request.json:
            contato_dao.save(request.json)
            return {"msg":"Contato salvo com sucesso."}
    return {"msg":"O contato não foi informado"}

@contato_routes.route("/api/v1/contato", methods=["GET"])
def obterTodosContatos():
    print("Metodo obterTodosContatos foi invocado")
    contacts = contato_dao.getAll()
    contactsList = []
    if len(contacts) > 0:
        for contact in contacts:
            contactOBJ = {}
            contactOBJ["id"] = contact[0]
            contactOBJ["nome"] = contact[1]
            contactOBJ["email"] = contact[2]
            contactOBJ["telefone"] = contact[3]
            contactsList.append(contactOBJ)
    return jsonify(contactsList)

@contato_routes.route("/api/v1/contato", methods=["PUT"])
def atualizar():
    print("Metodo Atualizar foi invocado")
    if request.json:
        if 'id' in request.json \
        and 'nome' in request.json \
        and 'email' in request.json \
        and 'telefone' in request.json:
            contato_dao.update(request.json)
            return {"msg":"Contato atualizado com sucesso."}
    return {"msg":"O contato não foi informado"}

@contato_routes.route("/api/v1/contato/<string:id>", methods=["DELETE"])
def remover(id):
    print("Metodo Remover foi invocado")
    if contato_dao.delete(id) == 1:
        return {"msg":"Contato removido com sucesso."}
    return {"msg":"O contato não foi removido"}
