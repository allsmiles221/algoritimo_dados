from pessoa import Pessoa

class Usuario(Pessoa):
    def __init__(self, nome):
        super().__init__(nome)

class UsuarioP(Pessoa):
    def __init__(self, nome, preferencial):
        super().__init__(nome)
        self.preferencial=preferencial
    