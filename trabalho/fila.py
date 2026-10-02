from collections import deque
from usuario import Usuario,UsuarioP



class Fila:
    def __init__(self):
        self.ListaUsuario=deque()

    def AdicionarLista(self, usuario):
        self.ListaUsuario.append(usuario)
    
    def RemoverProximo(self):
       if not (self.ListaUsuario):
           mensagem="não possui ninguem na fila"
           print(mensagem)
       else: 
            proximo=self.ListaUsuario.popleft()
            return proximo   