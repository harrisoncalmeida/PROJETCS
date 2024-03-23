'''
Em Python, variáveis são utilizadas para armazenar valores na memória do computador. Para criar uma variável, você precisa usar um nome e um valor. O nome da variável deve seguir as regras de nomenclatura do Python:

Deve começar com uma letra ou sublinhado (_).
Pode conter letras, números e sublinhados.
Não pode ser uma palavra-chave reservada do Python.
Para atribuir um valor a uma variável, utilize o operador de atribuição (=).

Exemplo:
'''
nome = 'Douglas'
print(nome)
print(type(nome))
idade = 48
print(idade)
print(type(idade))
altura = 1.85
print(altura)
print(type(altura))

'''
Tipos de Dados:

Cada variável em Python possui um tipo de dado, que define o tipo de valor que ela pode armazenar. Os tipos de dados mais comuns em Python são:

Inteiro (int): Números inteiros, como 1, 2, 3, etc.
Ponto flutuante (float): Números com casas decimais, como 1.5, 2.75, 3.14, etc.
String (str): Textos, como "Olá, mundo!", "Python é legal", etc.
Booleano (bool): Valores True ou False.

Conversão de Tipos:

É possível converter um tipo de dado para outro usando funções específicas.

Exemplo:
'''
nome = 'Douglas'
print(type(nome))
numero_inteiro = 10
print(type(numero_inteiro))
numero_float = float(numero_inteiro)  # Converte um inteiro para um float
print(type(numero_float))

'''
Os operadores aritméticos em Python permitem realizar operações matemáticas básicas, como adição, subtração, multiplicação, divisão e exponenciação. São ferramentas essenciais para qualquer programador Python, desde iniciantes até experientes.
'''
# Soma (+)
soma = 5 + 2
print(soma)

# Subtração (-)
menos = 5 - 2
print(menos)

# Multiplicação (*)
vezes = 5 * 2
print(vezes)

# Divisão (/)
dividir = 5 / 2
print(dividir)

# Parte Inteira da divisão (//)
inteiro = 5 // 2
print(inteiro)

# Resto da divisão (%)
resto = 5 % 2
print(resto)

# Exponenciação (**)
elevado = 5 ** 2
print(elevado)

'''
Os operadores de comparação em Python permitem verificar se duas expressões são iguais, diferentes, maiores, menores, etc. São ferramentas essenciais para tomar decisões e realizar comparações em seus programas. Retornam com resultado verdadeiro (True) ou Falso (False) (tipo bool)
'''
# Operador de Igualdade (==)
igualdade = 3 == 4
print(igualdade)

# Operador de Diferença (!=)
diferente = 3 != 4
print(diferente)

# Operador maior que (>)
maior = 3 > 4
print(maior)

# Operador menor que (<)
menor = 3 < 4
print(menor)

# Operador maior ou igual a (>=)
maior_igual = 3 >= 4
print(maior_igual)

# Operador menor ou igual a (<=)
menor_igual = 3 <= 4
print(menor_igual)

# Operador de identidade (is)
a = 7
b = 7.0
print(a is b)
print(a == b)

# Operador de identidade (is not)
a = 7
b = 7.0
print(a is not b)
print(a != b)

'''
Os operadores de associação in e not in em Python permitem verificar se um elemento está presente ou não em uma coleção, como listas, tuplas, dicionários e strings. São ferramentas úteis para filtrar dados e realizar comparações em seus programas. Assim como os aoperadores de comparação eles retornam Verdadeiro (True) ou Falso (False)
'''
# Operador in
nome = 'Douglas'
print('D' in nome)

# Operador not in
nome = 'Douglas'
print('D' not in nome)

'''
Os operadores lógicos em Python permitem combinar expressões booleanas (True ou False) para formar novas expressões booleanas. São ferramentas essenciais para tomar decisões e realizar comparações complexas em seus programas. São eles:

E (and): Retorna True se ambas as expressões forem True.
Exemplo: x > 0 and y < 10.

Ou (or): Retorna True se pelo menos uma das expressões for True.
Exemplo: x == 0 or y == 10.

Não (not): Inverte o valor da expressão.
Exemplo: not (x > 0).
'''

# Operador AND retorna verdadeiro se todas as condições forem verdadeiras
a = 3
b = 4
c = 5
print(a < b and b < c)
print(a < b and b > c)

# Operador OR retorna verdadeiro se pelo menos uma das condições for verdadeira
a = 3
b = 4
c = 5
print(a < b or b < c) # verdadeiro
print(a < b or b > c) # verdadiro
print(a > b or a > c) # Falso

# Operador not (inverte o resulta de verdadeiro para falso e de falso para verdadeiro)
a = 3
b = 4
c = 5
print(not(a > b))
print(not(a < b))

'''
As f-strings em Python são uma maneira concisa e elegante de formatar strings. Elas permitem incorporar expressões Python diretamente dentro de strings, tornando o código mais legível e fácil de manter.

Como usar f-strings:

Para usar f-strings, basta prefixar uma string literal com a letra "f". Dentro da string, você pode usar expressões Python entre chaves "{}":
'''
cliente = 'Douglas'
idade = 48
print(f'O nome do cliente é {cliente}, e ele tem {idade} anos de idade.')

taxa = 2/3
print(taxa)
print(f'O resultado da taxa é aproximadamente {taxa:.2f}')

'''
A função input() em Python permite que você obtenha entrada do usuário durante a execução do programa. É uma ferramenta essencial para interagir com o usuário e coletar dados para processamento.

Como usar a função input():

A função input() é simples de usar. Basta fornecer uma mensagem entre parênteses para instruir o usuário sobre o que digitar:
'''
nome = input('Informe seu primeiro nome: ')
print(f'Olá, {nome}!')

nome = input('Informe o seu primeiro nome: ')
massa = float(input('Informe seu peso em kg: '))
altura = float(input('Informe sua altura em metros na forma decimal: '))
imc = massa / (altura ** 2)
print(f'Olá {nome}! Seu IMC é {imc:.2f}')

'''
Este bloco traz possível soluções para quando queremos saber qual caracter temos em uma posição (índice) ou sequência de caracteres em um intervalo
'''
# 0    1   2   3   4   5  6  7  8  9 10 11 12 13 (índice)
# -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 (índice reverso)
# 1º 2º 3º 4º 5º 6º 7º 8º 9º 10º 11º 12º 13º 14º (ordinal)
# d  o  u  g  @  g  m  a  i   l   .   c   o   m


email = 'doug@gmail.com'
print(email[4])
print(email[:]) # imprimir um intervalo de todos os caracteres da string email
print(email[0:4]) # selecionando o intervalo a partir do índice 0 até o índice 3
print(email[2:]) # seleciona o intervalo a partir do índice 2 até o final
print(email[:5]) # seleciona o intervalo de todos os caracteres até o de índice 4
print(email[0:5:2]) # seleciona último caracter de uma sequência

'''
resumo do fatiamento de strings nome_variavel[indice de começo : índice de parada : de quanto em quanto] nome_variavel[início : fim : passo]
'''

# Contar a quantidade de carcteres em uma sequência
email = 'doug@gmail.com'
print(len(email))
qtde = len(email)
print(qtde)

cpf = 12345678910
print(type(cpf))
cpf = str(cpf)
print(type(cpf))

# Operador IN
email = 'doug@gmail.com'
print('u' in email)

# Operador NOT IN
email = 'doug@gmail.com'
print('u' not in email)

# Método capitalize converte em maiúscula apenas a primeira letra de uma string
nome = 'douglas'
print(nome)
nome = nome.capitalize()
print(nome)

# Método Title, serve para deixar a primeira letra de cada palavra maiúscula
nome = 'douglas almeida ribeiro'
print(nome)
nome = nome.capitalize()
print(nome)
nome = nome.title()
print(nome)

# Método upper deixa todas as letras em maiúscula
nome = 'Douglas de almeida ribeiro'
print(nome)
nome = nome.upper()
print(nome)

# Método para contar quantas vezes um determinado caracter aparece em uma string
email = 'doug@gmail.com'
email.count('@')

# Método que mostra a posição de um determinado caracter (caso apareça mais de uma vez, ele por padrão mostrará a 1ª)
email = 'doug@gmail.com'
email.find('o')

# Método startswith verifica se uma string começa com um determinado caracter ou sequência de caracteres
email = 'doug@gmail.com'
email.startswith('doug')

# Método endswith verifica se uma string termina com um determinado caracter ou sequência de caracteres
email = 'doug@gmail.com'
email.endswith('.com')

# Método isnumeric() verifica se o conteúdo de uma string é ou não numérico
cpf = '12345678910'
cpf.isnumeric()

# Método isalpha() verifica se o conteúdo de uma string é ou não letra
nome = 'Douglas Ribeiro'
nome.isalpha()

# Método isalnum verifica se o conteúdo de uma string é ou não combinação de letra e número
nome = 'Dougla5'
nome.isalnum()

# Método strip remove espaços indesejados no começo e/ou final da string
nome = ' Douglas '
print(len(nome))
nome = nome.strip()
print(len(nome))

# Método replace substitui um caracter por outro
# nome_da_string.replace('caracter_indesejado', 'caeacter_desejado')
preco = 'R$ 10.50'
preco = preco.replace('.',',')
print(preco)

# Método split (divide uma string em duas ou mais partes por meio de um separador)
nome = 'Douglas Almeida Ribeiro'
nomes = nome.split()
print(nomes)

# Método split (divide uma string em duas ou mais partes por meio de um separador)
date = '12/05/2023'
dia_mes_ano = date.split('/')
print(dia_mes_ano)

# Uma lista é um objeto que pode ser vazio, ou ter um ou mais itens
lista = ['dado1', 'dado2','dado3','dado4', 'dado_n']
#índices    0         1       2       3       4       ou:
#          -5        -4      -3      -2      -1
#           1º        2º      3º      4º      5º
'''
Qual é a informação presente na lista cuja posição é o
índice 3?
'''
print(f'A informação presente na lista na posição de índice 3 é: "{lista[3]}"')

'''
Quais dados estão presentes no intervalo que vai do 1º ao 3º elementos da lista?
'''
print(f'Os valores no intervalo do 1º ao 3º elementos são: "{lista[0:3]}"')

produtos = ['monitor', 'celular', 'notebook', 'desktop', 'impressora', 'teclado']
precos = [600, 2000, 5000, 3000, 1500, 200]
vendas = [300, 500, 100, 700, 500, 1000]
estoques = [5000] * 6 #  Este comando cria uma lista que tem 6 elementos com o mesmo valor (5000)

print(f'a lista produtos tem {len(produtos)} elementos')
print(f'a lista precos tem {len(precos)} elementos')
print(f'a lista vendas tem {len(vendas)} elementos')
print(f'a lista estoques tem {len(estoques)} elementos')

'''
Elabore um programa que receba do usuário um número inteiro e positivo de no máximo 5, e automaticamente, exiba o nome do produto correspondente, seu preço, sua quantidade vendida, o valor faturado em R$, e quantas unidades ainda restam em estoque desse produto.
'''

produtos = ['monitor', 'celular', 'notebook', 'desktop', 'impressora', 'teclado']
precos = [600, 2000, 5000, 3000, 1500, 200]
vendas = [300, 500, 100, 700, 500, 1000]
estoques = [5000] * 6 #  Este comando cria uma lista que tem 6 elementos com o mesmo valor (5000)

i = int(input('Informe um número inteiro e positivos de 0 a 5: ')) # recebe do usuário um número inteiro e positivo e o armazena na variável i
print(f'O produto escolhido foi: {produtos[i]}') # Exibe o nome do produto referente ao número informado pelo usuário
print(f'seu preço é de: R$ {precos[i]:,.2f}')
print(f'sua quantidade vendida fou de {vendas[i]} unidades')
print(f'o seu faturamento foi de R$ {(vendas[i]*precos[i]):,.2f} ')
print(f'e ainda restam {estoques[i]-vendas[i]} unidades em estoque')

i = int(input('Informe um número inteiro e positivos de 0 a 5: '))
print(f'''
O produto escolhido foi: {produtos[i]}, seu preço é de: R$ {precos[i]:,.2f},
sua quantidade vendida fou de {vendas[i]} unidades,
o seu faturamento foi de R$ {(vendas[i]*precos[i]):,.2f}, o seu faturamento
foi de R$ {(vendas[i]*precos[i]):,.2f}''')


