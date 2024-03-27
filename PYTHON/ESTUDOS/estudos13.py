# 1.0 VARIÁVEIS E TIPOS DE DADOS EM PYTHON

'''

1.1 Variáveis

Utilizamos variáveis em Python, para armazenar valores na memória do
computador. Podemos, criar uma variável da seguinte maneira (nome = valor).

Temos algumas regras de nomeclaturas para criação de variável:

1 - Deve começar com letras ou sublinhados, podendo conter números.
2 - Não pode ser uma palavra-chave reservada pelo Python.
3 - Para atribuir um valor a uma variável, utilize o operador de atribuição (=).

'''

# EXEMPLOS

nome = 'Harrison'
print(nome)

idade = 26
print(idade)

altura = 1.83 # Números com casas decimais utilizamos (.) no lugar da (,), então ficar atento.
print(altura)

'''

1.2 Tipo de variáveis

Cada variável em Python, possui um tipo de dado, que define o tipo de valor que
ela pode armazenar. Os tipo de dados mais comuns de Pyhton são:

Inteiro (Int): Contendo números inteiros. Ex.: 1,2,3,4,5,6 e etc.
Ponto flutuante (float): Contendo números com casa decimais. Ex.: 1.5,2.5,3.5,4.5 e etc.
String (str): Contendo textos em seus valores. Ex.: 'Harrison', 'Olá mundo' e etc.
Booleano (bool): Contendo resultados com True (verdadeiro) ou False (falso).

Observação: A gente pode também usar uma função chamada (type) dentro de um print para 
saber qual tipo de dado é aquela variável. Outra informação importante, é que podemos
transformar um tipo de dado de uma variável em outro tipo de dado. Irei exemplificar nos
exemplos abaixo. 

'''

# Exemplos

nome = 'Harrison'
print(type(nome))   # nessa variável vamos ter String (str), por ser um texto.

idade = 26
print(type(idade)) # nessa variável vamos ter Inteiro (int), por conter apenas números inteiros.

altura = 1.83
print(type(altura)) # nessa variável vamos ter Ponto flutuante (float), por conter casa decimais e números.

# Observação, assim que usamos a função (type), para retornar o tipo de dado daquela variável e utilizamos o (print) para imprimir aquele resultado da nossa variável.


# 2.0 OPERADORES PYTHON

'''

2.1 Operadores matemáticos

Operadores matemáticos em Python permitem realizar operações matemáticas básicas,
como adição, subtração, divisão, multiplicação e exponenciação. São operadores 
importantes para qualquer tipo de programador, seja ele avançado, intermediário e básico.

'''

# Soma (+)
soma = 7 + 5
print(soma)

# Subtração (-)
sub = 7 - 5
print(sub)

# multiplicação (*)
mult = 7 * 5
print(mult)

# Divisão (/)
divisao = 7 / 5
print(divisao)

# Divisão inteira (//)
divisao_int = 7 // 5
print(divisao_int)

# Resto da divisão (%)
resto = 7 % 5 
print(resto)

# Exponenciação (**)
elevado = 7 ** 5
print(elevado)

'''

2.2 Operadores de comparação

Operadores de comparações em Python, permite verificar se duas expressões são
iguais, diferentes, maiores, menores, etc. É importante para tomar decisões e 
realizar comparações em seus programas. Retornando como True (verdadeiro) ou False (falso)
são do tipo booleano (bool).

'''

# Operadores de igualdade (==)
igualdade = 3 == 4
print(igualdade)

# Operador de diferença (!=)
diferenca = 3 != 4
print(diferenca)

# Operador maior que (>)
maior = 3 > 4
print(maior)

# Operador menor que (<)
menor = 3 < 4
print(menor)

# Operador maior ou igual (>=)
maior_igual = 3 >= 4
print(maior_igual)

# Operador menor ou igual (<=)
menor_igual = 3 <= 4
print(menor_igual)

'''

2.3 Operadores de identidade

Operadores de identidade são usados para comparar os objetos, não se são iguais, mas se eles
forem realmente o mesmo objeto, com o mesmo local de memória,

(is) e (is not) são os operadores de identidade Python, são usados quando queremos chegar se dois valores (ou variáveis) estão localizados na mesma área de memória.

Observação: Duas variáveis iguais não significam que são idênticas!

1 - (is) True se os operadores são idênticos (referem ao mesmo objeto)
2 - (is not) True se os operadores não são idênticos (não referem ao mesmo objeto)

'''

# Exemplos com números:

x = 1
y = 1

print(x is y) # True
print(x is not y) # False

# Exemplos com strings:

a = 'Harrison'
b = 'Harrison'

print(a is b) # True
print(a is not b) # False

# Exemplos com listas:

x = [1,2,3]
y = [1,2,3]

print(x is y) # False
print(x is not y) # True

# Aqui vai uma observação para o exemplo de listas, quando tratamos com listas criadas independentemente uma da outra que foi o exemplo, não vamos ter as duas listas ocupando o mesmo espaço de memória. Mas a uma exceção, caso você crie uma lista e depois atribuí-la a outra variável, amabas as variáveis estarão se referindo ao mesmo objeto na memória.

# Exemplo da exceção com lista

x = [1,2,3]
y = x
print(x is y) # True

# Nesse caso vamos está atribuindo na variável (y) a variável (x), amabas vão está se referindo ao mesmo local da memória. Com isso, podemos dizer que que listas independentemente criada uma da outra, vamos ter o (is) retornando (False), pois as duas listas não estão ocupando o mesmo local da memória.

'''

2.4 Operadores de membros (associação)

Operadores de membros permitem verificar se um elemento está presente ou não em uma coleção,
como lista, tuplas, dicionários e strings. Ferramentas bastantes úteis para filtrar dados e realizar comparações em seus programas. 

1 - (in) Retorna True (verdadeiro) se o valor/variável é encontrada na sequência
2 - (in not) Retorna True (verdadeiro) se o valor/variável não está presente na sequência

'''

# Exemplos

# Operador in 
nome = 'Harrison'
print('r' in nome) # True (verdadeiro) pois ele encontra o (r) na string
print('k' in nome) # False (falso) pois ele não encontr o (z) na string

# Operador in not
nome = 'Harrison'
print('a' not in nome) # False (falso) pois o (a) encontra-se na string
print('k' not in nome) # True (verdadeiro) pois o (z) não encontra-se na string

'''

2.5 Operadores lógicos

Operadores lógicos permitem combinar expressões booleanas (True e False) para
formar novas expressões booleanas. São ferramentas essenciais para tomar decisões
e realizar comparações complexas em seus programas.

1 - (and) Retorna True (verdadeiro) se ambos os comandos são verdaeiros
2 - (or) Retorna True (verdadeiro) se um dos comandos é verdadeiro
3 - (not) Reverte o resultado, retornando False (falso) se o resultador for True (verdadeiro) e vice-versa

'''

# Exemplos

n1, n2, n3 = 3, 6, 7

print(n1 < n2 and n1 < n3) # True
print(n1 == n2 or n3 == n2) # False
print(not True) # False

# Exemplo AND

a = 3
b = 4
c = 5

print( a < b and b < c) # True
print( a > b and b > c) # False

# Exemplo OR

a = 3
b = 4
c = 5

print( a < b or b < c) # True
print( a < b or b > c) # True
print( a > b or b > c) # False

# Exemplo NOT

a = 3
b = 4
c = 5

print(not(a > b)) # True
print(not(a < b)) # False
