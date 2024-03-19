#Estrutura de repetição FOR(PARA)

for i in range(6):
    print(i)

#Estrutura de repetição FOR(PARA) - 1
for i in range(1,6,1):
    print(i)

#Estrutura de repetição FOR(PARA) - 2
for i in range(10,0,-2):
    print(i)

#Exercicio
soma = 0
qtd = 0
for i in range(1,101):
    if (i % 2 == 0):
        soma += i
        qtd += 1
media = soma / qtd
print("A media dos pares de 1 até 100 {}".format(media))