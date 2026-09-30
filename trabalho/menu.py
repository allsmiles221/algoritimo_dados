from fila import Fila, FilaPreferencial
from usuario import Usuario, UsuarioP


class Menu:
    def __init__(self):
        self.fila_normal = Fila()
        self.fila_preferencial = FilaPreferencial()

    def iniciar(self):
        while True:
            self.mostrarMenu()
            opcao = input("Escolha uma opcao: ").strip()

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
                print("Opcao invalida. Tente novamente.")

    def mostrarMenu(self):
        print("\n===== Caixa de Supermercado =====")
        print("1 - Entrar na fila")
        print("2 - Atender proximo cliente")
        print("3 - Ver fila atual")
        print("4 - Ver quantidade de pessoas na fila")
        print("5 - Sair")

    def entrarFila(self):
        nome = input("Digite o nome do cliente: ").strip()

        if nome == "":
            print("Nome vazio. Cliente nao foi adicionado.")
            return

        resposta = input("Possui atendimento preferencial? (s/n): ").strip().lower()

        if resposta == "s":
            tipo_preferencial = input("Informe o tipo de preferencia (idoso, gestante, PCD): ").strip()
            usuario = UsuarioP(nome, tipo_preferencial)
            self.fila_preferencial.entrarFila(usuario)
            print("Cliente adicionado na fila preferencial.")
        elif resposta == "n":
            usuario = Usuario(nome)
            self.fila_normal.entrarFila(usuario)
            print("Cliente adicionado na fila normal.")
        else:
            print("Resposta invalida. Cliente nao foi adicionado.")

    def atenderProximo(self):
        cliente = self.fila_preferencial.removerProximo()

        if cliente is not None:
            print("Cliente atendido:", cliente.nome)
            return

        cliente = self.fila_normal.removerProximo()

        if cliente is not None:
            print("Cliente atendido:", cliente.nome)
        else:
            print("Nao existem clientes aguardando.")

    def verFilaAtual(self):
        print("\nFila preferencial:")
        self.mostrarClientes(self.fila_preferencial.obterFila())

        print("\nFila normal:")
        self.mostrarClientes(self.fila_normal.obterFila())

    def mostrarClientes(self, clientes):
        if len(clientes) == 0:
            print("[]")
            return

        for cliente in clientes:
            print(cliente.nome)

    def verQuantidadeFila(self):
        quantidade_preferencial = self.fila_preferencial.quantidade()
        quantidade_normal = self.fila_normal.quantidade()
        quantidade_total = quantidade_preferencial + quantidade_normal

        print("Quantidade na fila preferencial:", quantidade_preferencial)
        print("Quantidade na fila normal:", quantidade_normal)
        print("Quantidade total:", quantidade_total)

    def sair(self):
        print("Programa encerrado. Ate logo!")
