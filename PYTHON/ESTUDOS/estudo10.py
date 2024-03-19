#Exemplo 1
mochila = ("Machado", "Camisa", "Bacon", "Abacate")
print(mochila)

#Exemplo 2
print(mochila[0])  # print do Elemento 1 - Índice 0
print(mochila[2])  # print do Elemento 3 - Índice 2
print(mochila[0:2])  # print do Elemento 1 e 2 - Índice 0 e 1
print(mochila[2:])  # print dos Elemento a partir do índice 2
print(mochila[-1])  # print do último

#Exemplo 3
mochila[2] = "Ovos"  # Vai dar erro, pois uma tupla não conseguimos mudar o que já foi colocado

#Exemplo 4
for item in mochila:
    print("Naminha mochila tem: {}".format(item))

#Exemplo 5
tam = len(mochila)
for i in range (0, tam, 1):
    print("Na minha mochila tem: {}".format(mochila[i]))

#Exemplo 6
mochila = ("Machado", "Camisa", "Bacon", "Abacate")
upgrade = ("Queijo", "Canivete")
mochila_grande = mochila + upgrade

print(mochila)
print(upgrade)
print(mochila_grande)

#Exemplo 7 - Desempacotamento de parâmentros em funções
def soma(*num):
    soma = 0
    print("Tupla: {}".format(num))
    for i in num:
        soma += i
        return soma

print("Resultado: {}\n".format(soma(1,2)))
print("Resultado: {}\n".format(soma(1,2,3,4,5,6,7,8,9)))