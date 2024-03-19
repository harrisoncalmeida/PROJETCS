#Retorno de valores em funções
def soma(x = 0, y = 0, z = 0):
    res = x + y + z
    return res

#Programa principal
retornado = soma(1,2,3)
print(retornado)

#Forma alternativa simplificada
print(soma(2,2))

#Programa principal
retornando1 = soma(1,2,3)
retornando2 = soma(1,2)
retornando3 = soma()
print("Somatórios: {}, {} e {}:".format(retornando1, retornando2, retornando3))

#Exercício
def valida_string(pergunta, min, max):
    s1 = input(pergunta)
    tam = len(s1)
    while ((tam < min) or (tam > max)):
        s1 = input(pergunta)
        tam = len(s1)
    return s1

#Programa principal
x = valida_string("Digite uma string:", 10, 30)
print("Você digitou a string: {}. \n Dado válido. Encerrando o programa...".format(x))