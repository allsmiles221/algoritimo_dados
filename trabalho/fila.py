from collections import deque


class Fila:
    def __init__(self):
        self.listaUsuario = deque()

    def entrarFila(self, usuario):
        self.listaUsuario.append(usuario)

    def removerProximo(self):
        if self.quantidade() == 0:
            return None

        return self.listaUsuario.popleft()

    def obterFila(self):
        return list(self.listaUsuario)

    def quantidade(self):
        return len(self.listaUsuario)


class FilaPreferencial:
    def __init__(self):
        self.listaUsuarioP = deque()

    def entrarFila(self, usuario):
        self.listaUsuarioP.append(usuario)

    def removerProximo(self):
        if self.quantidade() == 0:
            return None

        return self.listaUsuarioP.popleft()

    def obterFila(self):
        return list(self.listaUsuarioP)

    def quantidade(self):
        return len(self.listaUsuarioP)
