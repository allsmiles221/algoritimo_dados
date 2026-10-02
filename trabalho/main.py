#from menu import Menu
from usuario import Usuario,UsuarioP
from fila import Fila,FilaPreferencial

Usuario1=Usuario("Test")
UsuarioP2=UsuarioP("Alefe","PCD")

fila=Fila()
fila.AdicionarLista(Usuario1)

print(f"aqui está fila {fila.getFila[Usuario1.getNome()]}")

