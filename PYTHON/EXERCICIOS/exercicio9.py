#Exemplo Lista
mochila = ("Machado", "Camisa", "Bacon", "Abacate")
print("Tupla:", mochila)
mochila = ["Machado", "Camisa", "Bacon", "Abacate"]
print("Lista:", mochila)

#Exemplo 1
mochila[2] = "Laranja"
print("Tupla:", mochila)

#Exemplo 2
mochila.append("Ovos")
print("Lista:", mochila)

#Exemplo 3
mochila.insert(1, "Canivete")
print("Lista:", mochila)

#Exemplo 4
del mochila[1]
print("Lista:", mochila)
mochila.remove("Ovos")
print("Lista:", mochila)

#Exemplo
x = [5, 7, 9, 11]
y = x[:]  # Esses dois pontos dentro de uma caixa, vai fazer com quem crie uma cópia diferente na memória do trabalho. Serve para fazer uma cópia.
print(x)
print(y)
