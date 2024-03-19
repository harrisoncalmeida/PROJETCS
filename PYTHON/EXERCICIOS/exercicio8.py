def imprime_com_condicao(num, fcond):
    if fcond(num):
        print(num)
def par(x):
    return x % 2 == 0
def impar(x):
    return not par(x)

#Programa principal
imprime_com_condicao(5, impar)

#Função lambda
res = lambda x: x * x
print(res(3))

soma = lambda x, y: x +y
print(soma(3,5))