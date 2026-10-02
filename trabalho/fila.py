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

    def getFila(self):
        return list(self.ListaUsuario)
    
    def quantidadeFila(self):
        return len(self.ListaUsuario)
class FilaPreferencial:

    def __init__(self):
        self.ListaUsuarioP=deque()

    def AdicionarLista(self, usuario):
        self.ListaUsuarioP.append(usuario)
    
    def RemoverProximo(self):
       if not (self.ListaUsuarioP):
           mensagem="não possui ninguem na fila"
           print(mensagem)
       else: 
            proximo=self.ListaUsuarioP.popleft()
            return proximo   

    def getFila(self):
        return list(self.ListaUsuarioP)
    
    def quantidadeFila(self):
        return len(self.ListaUsuarioP)