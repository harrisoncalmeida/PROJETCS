#Exemplo de Strings e listas dentro de listas
mochila = ("Machado", "Camisa", "Bacon", "Abacate")
print(mochila[0])

#Exemplo 1
mochila = ("Machado", "Camisa", "Bacon", "Abacate")
print(mochila[0][0])
print(mochila[2][1])

#Exemplo 2
mochila = ("Machado", "Camisa", "Bacon", "Abacate")
for item in mochila:
    for letra in item:
        print(letra, end="")
    print()

#Exemplo 3 é memsa resolução do exemplo 2, só são maneira diferentes de resolver o problema
mochila = ("Machado", "Camisa", "Bacon", "Abacate")
for i in range(0,len(mochila),1):
    for j in range(0,len(mochila[i]),1):
        print(mochila[i][j], end="")
    print()

#Exemplo 4
item = []
mercado = []

for i in range(3):
    item.append(input("Digite o nome do item:"))
    item.append(int(input("Digite a quantidade:")))
    item.append(float(input("Digite o valor:")))
    mercado.append(item[:])
    item.clear()
print(mercado)

#Exemplo 5 maneira mais simplificada de resolver, mas é mesma coisa do exemplo 4
mercado = []

for i in range(3):
    nome = input("Digite o nome do item:")
    qtd = int(input("Digite a quantidade:"))
    valor = float(input("Digite o valor:"))
    mercado.append([nome, qtd, valor])
print(mercado)

#Exemplo 6
soma = 0
print("Lista de compras:")
print("-" * 20)
print("item | quantidade | valor unitário | total do item")
for item in mercado:
    print("{} | {} | {} | {}".format(item[0], item[1], item[2], item[1] * item[2]))
    soma += item[1] * item[2]
print("-" * 20)
print("Total a ser pago: {}".format(soma))

