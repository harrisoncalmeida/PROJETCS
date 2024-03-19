resultado = 1387 % 19 == 0
print(resultado)

numero = 31
resultado = numero % 2 == 0
print(resultado)

numero = [34, 29, 31]
menor_valor = min(numero)
resultado = menor_valor < 30
print(resultado)

#Exercício

#if (idade > 60):
   # print('Você tem direito aos beneficios!')

#if (dano > 10 and escudo == 0):
    #print('Você está morto!')

#if (norte or sull or leste or oeste or):
    #print('Você escapou!')

ano = int(input('Digite um ano:'))
if ano % 4 == 0:
    print('Pode ser um ano bissexto')
else:
    print('Definitivamente não é um ano bissexto')

cima = True
baixo = True

if cima and baixo:
    print('Decida-se!')
else:
    print('Você escolheu um caminho!')

#Exercício

A = int(input('Digite o 1º lado do triângulo:'))
B = int(input('Digite o 2º lado do triângulo:'))
C = int(input('Digite o 3º lado do triângulo:'))

if A > 0 and B > 0 and C > 0:
    if A + B > C and A + C > B and B + C > A:
    # Se você chegou até aqui, é porque o triângulo é valido!
        if A != B and A != C and B != C:
            print("Triângulo escaleno!")
        else:
            if A == B and A == C and B == C:
                print("Triângulo equilátero!")
            else:
                print('Triângulo isósceles!')
    else:
        print('Ao menos um dos valores indicados não servem para formar um triângulo')
else:
    print('Ao menos um dos valores indicados não servem para formar um triângulo')