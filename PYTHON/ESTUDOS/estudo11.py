dadosx = input('Informe os valores de x separados por espaços: ')
dadosy = input('''Informe os valores de y separados por espaços
(informe a mesma quantidade de dados informados em x): ''')
x = dadosx.split()
y = dadosy.split()
xq = []
yq = []
xy = []
for i in range(len(x)):
  x[i] = float(x[i])
  y[i] = float(y[i])
  xq.append(x[i]**2)
  yq.append(y[i]**2)
  xy.append(x[i]*y[i])
n = len(x)
sx = sum(x)
sy = sum(y)
sxq = sum(xq)
syq = sum(yq)
sxy = sum(xy)
r = (sxy - (sx * sy / n)) / ((sxq - sx**2/n) * (syq - sy**2/n))**(1/2)
rq = r**2
if rq > 0.5:
  if r > 0:
    print(f'O coeficiente de correlação é {r:.4f} e indica forte correlação positiva')
  else:
    print(f'O coeficiente de correlação é {r:.4f} e indica que temos forte correlação negativa')
else:
  print(f'O coeficiente de correlação é {r:.4f} e indica baixa correlação')

'''
Imagine que você deseja utilizar uma estrutura for combinada com a função range
para percorrer e imprimir uma sequência de tamanho 10, ou seja, que como saída
tenhamos 10 prints de 10 números diferentes
'''
for i in range(10):
  print(f'O {i+1}º valor é {i}')

'''
Imagine que na mesma situação do exercício anterior você
deseja interromper o ciclo de impressões após o programa ter
impresso 5 valores diferentes
'''
for i in range(10):
  if i == 5:
    break
  print(f'O {i+1}º valor é {i}')

'''
Ainda imaginando a situação original, suponha que você deseja imprimir
toda a sequencia exceto um determinado valor, por exemplo o 5
'''
for i in range(10):
  if i == 5:
    continue
  print(f'O {i+1}º valor é {i}')

'''
Imagine que você deseja que o programa ignore a parada estabelecida pelo if
'''
for i in range(10):
  if i == 5:
    pass
  print(f'O {i+1}º valor é {i}')

'''
Imagine que você deseja criar um programa que receba do usuário um número
inteiro que defina quantas vezes será impressa a expressão "olá mundo!" e depois
imprima essa expressão exatamente na quantidade informada pelo usuário
'''

# Solução 01
n = int(input('Informe quantas vezes você deseja ver a mensagem olá mundo: '))
c = 0
while c < n:
  print('Olá Mundo!')
  c += 1

# Solução 02 usando while True
n = int(input('Informe quantas vezes você deseja ver a mensagem olá mundo: '))
c = 0
while True:
  if c < n:
    print('Olá Mundo!')
    c += 1
  else:
    break
  
'''
O while True é uma estrutura mais flexível que o while pois não traz a condição
na própria lina de declaração while, permitindo assim, que você faça várias
outras condições aninhadas logo abaixo da declaração while True.
'''

# Exercício

'''
Elabore um programa que que receba um número inteiro e positivo do usuário e
verifique se o número informado é par ou ímpar, se for par imprima uma mensagem
dizendo que o número é par e encerre o loop, caso seja ímpar exiba uma mensagem
informando que o número não é par e peça para o usuário digitar outro número,
até que o número digitado pelo usuário seja par.
'''

while True:
  n = int(input('Informe um número par inteiro e positivo: '))
  if n % 2 == 0:
    print(f'O número {n} é um número par! Parabéns!')
    break
  else:
    print(f'O número {n} não é um número par, favor informe um número par')

'''
Elabore um programa que receba do usuário um número qualquer e exiba a mensagem:
Parabéns você digitou um número!
'''

while True:
  try:
    n = float(input('Informe um número qualquer: '))
    print('Parabéns você digitou um número!')
    break
  except:
    print('o valor informado não é um número')

'''
Imagine que você tem uma lista com seis nomes de pessoas e outra com seis idades
Suponha que a posição de cada nome em sua lista corresponde a mesma posição
da sua idade na lista idades. Elabore um código que percorra as duas listas,
verifique se a pessoa é maior ou menor de idade (18 anos) e exiba uma mensagem
com cada nome, sua idade e um texto informando se essa pessoa é maior ou menor
de idade.
'''
nomes = ['Douglas','Daniela','Pedro','Maria','Eduardo','Ester']
idades = [48, 9, 70, 70, 44, 37]
for i in range(len(nomes)):
  if idades[i] >= 18:
    print(f'{nomes[i]} tem {idades[i]} anos e é maior de idade')
  else:
    print(f'{nomes[i]} tem {idades[i]} anos e é menor de idade')

'''
Imagine que você tem uma lista com seis nomes de pessoas e outra com seis idades
Suponha que a posição de cada nome em sua lista corresponde a mesma posição
da sua idade na lista idades. Elabore um código que percorra as duas listas,
verifique se a pessoa é maior ou menor de idade (18 anos) e exiba uma mensagem
com cada nome, sua idade e um texto informando se essa pessoa é maior ou menor
de idade.
'''
nomes = ['Douglas','Daniela','Pedro','Maria','Eduardo','Ester']
idades = [48, 9, 70, 70, 44, 37]
for i,v in enumerate(idades):
  if idades[i] >= 18:
    print(f'{nomes[i]} tem {v} anos e é maior de idade')
  else:
    print(f'{nomes[i]} tem {v} anos e é menor de idade')

'''
Imagine que você deseja criar um programa que receba do usuário o valor de um
determinado produto e a informação se esse produto é nacional ou importado e
retorne para o usuário o valor do imposto a pagar. Considere que se o produto
for nacional a alíquota de imposto é de 18% para valores até R$ 200,00 e 25%
para valores acima de R$ 200,00. Agora se o produto for importado é isento para
valores até R$ 200,00 e pagará 35% para valores acima de R$ 200,00.
'''

while True:
  try:
    valor = float(input('Informe o valor do produto em R$ '))
    break
  except:
    print('valor inválido')
nac = input('O produto é nacional? 1 para sim ou 2 para não: ')
if nac == '1':
  if valor <= 200:
    imposto = valor * 0.18
  else:
    imposto = valor * 0.25
else:
  if valor > 200:
    imposto = valor * 0.35
  else:
    imposto = 0
print(f'O valor do imposto é R$ {imposto:.2f}')

'''
Elabore um programa que receba do usuários duas sequencias de números separados
por espaços com igual quantidade sendo uma sequência em um único input e outra
sequência em outro input único
'''
dadosx = input('Informe uma sequência de números separados por espaços: ')
dadosy = input('''Informe outra sequência de números separados por espaços com a
mesma quantidade informada na primeira: ''')

'''
Agora separe cada sequência em uma lista, exemplo: dadosx separado em uma lista
camada x e dadosy em uma lista chamada y
'''
x = dadosx.split()
y = dadosy.split()

'''
percorra cada uma das listas criadas e para cada valor encontrado converta-o em
um tipo float
'''
for i in range(len(x)):
  x[i] = float(x[i])
for i in range(len(y)):
  y[i] = float(y[i])

'''
Agora crie três listas vazias, sendo xq, yq e xy e as preencha da sequinte forma:

1 - xq: percorra a lista de x e para cada valor encontrado o eleve ao
quadrado e guarde-o na lista xq

2 - yq: percorra a lista de y e para cada valor encontrado o eleve ao
quadrado e guarde-o na lista yq

3 - xy:  percorra a lista de x e a de y e multiplique cada valor de x pelo
seu valor de y correspondente e guarde os resultados na lista xy
'''
xq = []
yq = []
xy = []
for i in range(len(x)):
  xq.append(x[i]**2)
for i in range(len(y)):
  yq.append(y[i]**2)
for i in range(len(x)):
  xy.append(x[i]*y[i])
'''
Agora vamos criar uma variável que armazena o resultado da lista, sendo:
sx = soma dos valores da lista x
sy = soma dos valores da lista y
sxq = soma dos valores da lista xq
syq = soma dos valores da lista yq
sxy = soma dos valores da lista xy
n = a quantidade de elementos de um das listas
mediax = a média da lista x
mediay = a média da lista y
'''
sx = sum(x)
sy = sum(y)
sxq = sum(xq)
syq = sum(yq)
sxy = sum(xy)
n = len(x)
mediax = sx/n
mediay = sy/n

beta = (sxy - (sx * sy /n)) / (sxq - sx**2 / n)
a = mediay - beta * mediax
print(f'A equação da reta de regressão linear simples é Y = {a:.1f} + {beta:.1f} * x')