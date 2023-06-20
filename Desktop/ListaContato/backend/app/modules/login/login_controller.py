
class LoginController:

    def logar(self, email, senha):
        if email == "admin@gruponobre.edu.br" \
        and senha == "adminpw":
            return True
        return False