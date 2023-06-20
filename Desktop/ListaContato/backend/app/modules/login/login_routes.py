from flask import Blueprint, request
from app.modules.login.login_controller import LoginController
from app.security.security_controller import SecurityController

login_routes = Blueprint("login",__name__)

@login_routes.route("/api/v1/login", methods=["POST"])
def logar():
    if(request.json):
        if 'email' in request.json \
        and 'senha' in request.json:
            loginBC = LoginController()
            estaLogado = loginBC.logar(request.json['email'],request.json['senha'])
            if estaLogado:
                securityBC = SecurityController()
                return {"token":securityBC.criarToken(request.json['email'])}
            return {"msg":"Falha no login"}
        return {"msg":"Faltando parâmetros: email ou senha"}
    return {"msg":"Nenhum parâmetro foi informado"}