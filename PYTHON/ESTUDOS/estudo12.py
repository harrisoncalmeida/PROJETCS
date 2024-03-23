'''
Imagine que você deseja criar uma função que imprima o "Olá!" todas as vezes que essa função for executada, sem ter a necessidade de usar o print, por
exemplo
'''
def oi():
  print('Olá!')
'''
O processo de criação de uma função é muito simples, devemos começar com a palavra reservada "def" seguido de um nome que vamos usar para chamar a função e dpois parenteses para especificar os argumentos da função, lembrando que os argumentos de uma função, são opcionais, observe que no caso de função do exemplo acima, não temos argumentos obrigatórios, e além disso, essa função não
possui retorno
'''

'''
Suponha agora que você deseja guardar o texto de saída da função acima em uma variável qualquer
'''
#oi()

'''
Observe que a função cumpre o seu papel, ou seja, quando executada, exibe no console o texto "Olá!"
'''

'''
agora vamos tentar guardar esse texto em uma variável chamada texto
'''

texto = oi()
print(texto)

'''
Nesse caso não temos nada guardado na variável texto pq essa função não tem retorno
'''

def oi():
  return 'Olá!'
'''
Agora a função oi possui como retorno o texto 'Olá!'
e como ela tem retorno esse retorno pode ser armazenado
em uma variável, por exemplo
'''

texto = oi()
print(texto)

'''
Imagine que você precisa fazer uma função que calcula automaticamente o valor total do desconto sobre o valor da compra de um cliente, e esse desconto total, depende de diferentes percentuais que podem ser aplicados sobre o valor total
da compra do cliente, tais percentuais podem ser referentes a cupon de desconto, pagamento à vista em pix, clube de vantagens vip e desconto para professores. suponha que nossos clientes possuem todos os descontos e as taxas são fixas: cupon 1% pix 2%
vip 3% rof 4%
'''

def desconto(valor):
  cupon = valor * 0.01
  pix = valor * 0.02
  vip = valor * 0.03
  prof = valor * 0.04
  return cupon + pix + vip + prof

print(f'O valor do desconto na sua compra foi de R$ {desconto(1000)}')

'''
Formatações de código limpo para Python
'''


# Forma que consegui fazer direito
a = [1.85,1.23,1.75,1.67,1.82,1.73]
p = [70,22,87,64,96,68]

imc = [p / a**2 for a, p in zip(a, p)]

for i, imc in enumerate(imc):
  print(f'A pessoa {i+1} tem IMC de: {imc:.2f}')


# outra forma
a = [1.85,1.23,1.75,1.67,1.82,1.73]
p = [70,22,87,64,96,68]

imc = []
for i in range(len(p)):
  imc.append(round(p[i]/a[i]**2,2))
print(f'A pessoa tem IMC de: {imc}')