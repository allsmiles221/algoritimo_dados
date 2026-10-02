from fila import Fila, FilaPreferencial
from usuario import Usuario, UsuarioP


class Menu:
    def __init__(self):
        self.fila = Fila()
        self.filaPreferencial = FilaPreferencial()

    def iniciar(self):
        while True:
            print("\n1 - Entrar na fila")
            print("2 - Atender proximo cliente")
            print("3 - Ver fila atual")
            print("4 - Ver quantidade de pessoas na fila")
            print("5 - Sair")

            opcao = input("Escolha uma opcao: ")

            if opcao == "1":
                self.entrarFila()
            elif opcao == "2":
                self.atenderProximo()
            elif opcao == "3":
                self.verFilaAtual()
            elif opcao == "4":
                self.verQuantidadeFila()
            elif opcao == "5":
                self.sair()
                break
            else:
                print("Opcao invalida.")

    def entrarFila(self):
        nome = input("Digite o nome: ")

        if nome == "":
            print("Nome vazio.")
            return

        resposta = input("Possui atendimento preferencial? (s/n): ")

        if resposta == "s":
            preferencial = input("Digite o tipo de preferencia (idoso, gestante, PCD): ")
            usuario = UsuarioP(nome, preferencial)
            self.filaPreferencial.AdicionarLista(usuario)
            print("Usuario adicionado na fila preferencial.")
        elif resposta == "n":
            usuario = Usuario(nome)
            self.fila.AdicionarLista(usuario)
            print("Usuario adicionado na fila normal.")
        else:
            print("Resposta invalida.")

    def atenderProximo(self):
        if self.filaPreferencial.quantidadeFila() > 0:
            usuario = self.filaPreferencial.RemoverProximo()
            print("Atendendo:", usuario.getNome())
        elif self.fila.quantidadeFila() > 0:
            usuario = self.fila.RemoverProximo()
            print("Atendendo:", usuario.getNome())
        else:
            print("Nao ha ninguem para atender.")

    def verFilaAtual(self):
        print("\nFila preferencial:")
        self.mostrarFila(self.filaPreferencial.getFila())

        print("\nFila normal:")
        self.mostrarFila(self.fila.getFila())

    def mostrarFila(self, lista):
        if len(lista) == 0:
            print("[]")
        else:
            i = 0
            while i < len(lista):
                usuario = lista[i]
                print(usuario.getNome())
                i = i + 1

    def verQuantidadeFila(self):
        quantidadePreferencial = self.filaPreferencial.quantidadeFila()
        quantidadeNormal = self.fila.quantidadeFila()
        total = quantidadePreferencial + quantidadeNormal

        print("Fila preferencial:", quantidadePreferencial)
        print("Fila normal:", quantidadeNormal)
        print("Total:", total)

    def sair(self):
        print("Programa encerrado.")
