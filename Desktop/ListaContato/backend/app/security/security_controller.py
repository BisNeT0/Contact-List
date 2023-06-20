import jwt

class SecurityController:

    def criarToken(self, email):
        return jwt.encode({"email":email},"peixeskol",algorithm="HS256")
    
    def decodificarToken(self, token):
        return jwt.decode(token, "peixeskol", algorithm="HS256")
