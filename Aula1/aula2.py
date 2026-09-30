#pessoa=("Ana", 25,1.65)
#print(f"Nome: {pessoa[0]}, idade: {pessoa[1]}, Altura:{pessoa[2]}")


# nome= input("Adicione seu nome")

# idade= input("Adicione seu idade")

# cidade= input("Adicione seu cidade")

# pessoa=(nome, idade, cidade)

# print (pessoa)

# frutas=["maçã","banana", "uva"]
# print(frutas[0])
# print(frutas[2])

# numeros=[1,2,3,4]
# numeros[2]=99
# print(numeros)

lista=[]

print("Digite os elementos da lista. ")
print("Digite 'sair' para encerrar a entrada. ")

while True:
    item=input("Digite um valor: ")
    if item.lower()=='sair':
        break
    lista.append(item)

print("\nAlista criada foi: ")
print(lista)