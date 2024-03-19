'''
Alternativa usando o range
'''

notas = input('Informe as notas de 0 a 10 separadas por espaços: ')
notas = notas.split()
for i in range(len(notas)):
  notas[i] = float(notas[i])
media = sum(notas)/len(notas)
print(media)
if media == 10:
  print('Parabéns você foi aprovado com nota máxima!')
else:
  if media >= 6:
    print('Parabéns você foi aprovado!')
  elif media >= 4:
    print('Você ficou de recuperação!')
  else:
    print('Infelizmente você não foi aprovado!')

'''
Alternativa usando enumerate
'''

notas = input('Informe as notas de 0 a 10 separadas por espaços: ')
notas = notas.split()
for i, v in enumerate(notas): # "i" de índice e "v" de valor
  notas[i] = float(v)
media = sum(notas)/len(notas) # "sum" para somar "len" contar caracteres em uma string
print(media)
if media == 10:
  print('Parabéns você foi aprovado com nota máxima!')
else:
  if media >= 6:
    print('Parabéns você foi aprovado!')
  elif media >= 4:
    print('Você ficou de recuperação!')
  else:
    print('Infelizmente você não foi aprovado!')


#Laço While
    
n = int(input('Informe um número inteiro que representa a quantidade de notas que deseja informar: '))
c = 0
ns = []
while c < n:
  ns.append(float(input(f'Informe a {c+1}ª a nota 0 a 10: ')))
  c += 1
print(ns)


# Outra informação 
dadosx = input('Informe os valores de x separados por espaços: ')
dadosy = input('Informe os valores de y separados por espaços (Informe a mesma quantidade de "x"): ')
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

  