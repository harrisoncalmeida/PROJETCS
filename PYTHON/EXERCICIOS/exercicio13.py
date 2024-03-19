print('Olá mundo!')
print(2+5)

#Exercício Expressões algébricas

#a) 1 + 2 + 3 + 4 + 5
#b) (23 + 19 + 31) / 3
#c) 403 // 73
#d) %
#e) 2**10 - ** pontencia
#f) abs(54-75) - abs ignora o sinal
#g) print(min(34, 29, 31)) - min serve para o valor minimo

#Exercício Atribuição

#a) a = 3 - um sinal de igual atribuição
#b) b = 4
#c) c = a*a + b*b

#Exercício Strings

#s1 = 'ant'
#s2 = 'bat'
#s3 = 'cod'

#print(s1 + ' ' + s2 +' ' + s3)
#print(10*(s1 + ' '))
#print(1*(s1 + ' ') + 2*(s2 + ' ') + 3*(s3 + ' '))
#print((2 * s2) + s3)

#Exercício 1

#preco = float(input('Digite o preço do produto:')) #float serve para um ponto flutuante.
#p = float(input('Digite o percentual de desconto (0-100)%:'))

#desconto = preco * (p / 100)
#final = preco - desconto

#print('O preço do produto é {}. Desconto de {}%.'.format(preco, p))
#print('Valor calculado de desconto: {}. Valor final do produto: {}'.format(desconto, final))

#Exercício 2

#km = int(input('Quantos km foram percorridos?')) #int varial de número inteiros, strings.
#dias = int(input('Por quantos dias ele foi alugado?'))

#preco = 60 * dias * 0.15 * km
#print('Km = {}. Dias: {}'. format(km, dias))
#print('Valor a ser pago: {}'.format(preco))

#Exercício 3

frase = input('Digite uma frase:')
tam = len(frase)

frase2 = frase[:int(tam/1)]
print(frase2[-2:])