'''
Inserindo valores em uma lista
'''

produtos = ['monitor', 'celular', 'notebook', 'desktop', 'impressora', 'teclado']
precos = [600, 2000, 5000, 3000, 1500, 200]
vendas = [300, 500, 100, 700, 500, 1000]
estoques = [5000] * 6

'''
Inserindo um novo produto na lista de produtos
'''
produtos.append('mouse') # append, vou utilizar quando eu quero acrescenter um novo produto em minha lista
print(produtos)
precos.append(10)
print(precos)

'''
Inserindo valores em um índice específico de uma lista
'''
produtos = ['monitor', 'celular', 'notebook', 'desktop', 'impressora', 'teclado']
precos = [600, 2000, 5000, 3000, 1500, 200]
vendas = [300, 500, 100, 700, 500, 1000]
estoques = [5000] * 6 #  Este comando cria uma lista que tem 6 elementos com o mesmo valor (5000)
'''
método insert Imagine que você deseja inserir o produto 
microfone na primeira posição da lista (índice 0), sem 
excluir nenhum produto previamente existente
'''
produtos.insert(0,'microfone')
print(produtos)
precos.insert(0,700)
print(precos)
vendas.insert(0,50)
print(vendas)
estoques.insert(0,5000)
print(estoques)

'''
A principal diferença entre append e insert é a posição que o elemento é
inserido, no append por padrão o elemento é inserido na última posição e no
insert é possível escolher a posição onde vamos inserir o novo elemento
'''

'''
Utilizando o método remove para excluir um dado pelo seu valor
'''
produtos = ['monitor', 'celular', 'notebook', 'desktop', 'impressora', 'teclado']
precos = [600, 2000, 5000, 3000, 1500, 200]
vendas = [300, 500, 100, 700, 500, 1000]
estoques = [5000] * 6 #  Este comando cria uma lista que tem 6 elementos com o mesmo valor (5000)

'''
Suponha que você deseja remover o teclado da lista produtos e não saiba qual é
o seu índice
'''
produtos.remove('teclado')
print(produtos)
precos.remove(200)
print(precos)

'''
Suponha que você deseja saber se na lista produtos existe o termo celular
'''
produtos = ['monitor', 'celular', 'notebook', 'desktop', 'impressora', 'teclado']
precos = [600, 2000, 5000, 3000, 1500, 200]
vendas = [300, 500, 100, 700, 500, 1000]
estoques = [5000] * 6 #  Este comando cria uma lista que tem 6 elementos com o mesmo valor (5000)

print('celular' in produtos)

'''
Suponha que você deseja saber se na lista produtos existe o termo celular e caso
exista qual é o seu índice - método index
'''
produtos.index('celular')
i = produtos.index() # essa como serve para guardar na variável "i"
i = produtos.index(input('Informe nome do produto que deseja consultar: ')) # esse é para que o úsuario informe o produto que quer consultar
# ".lower()" esse serve para que todos os dados que venham do input com letras minusculas 

'''
Tuplas são estruturas de dados imutáveis
'''
# Criando tuplas
nomes = ('Douglas', 'Daniela', 'Pedro', 'Maria')
idades = (47, 8, 68, 67)
alturas = (1.85, 1.32, 1.75, 1.69)
tupla_vazia = ()
print(type(nomes))
print(nomes)

# Fatiando tuplas
nomes = ('Douglas', 'Daniela', 'Pedro', 'Maria')
idades = (47, 8, 68, 67)
alturas = (1.85, 1.32, 1.75, 1.69)
print(nomes[0])
print(idades[1:3])
print(alturas[-1])

# convertendo objetos em tuplas e vice-versa
lista = [1,2,3]
tupla = tuple(lista)
nova_lista = list(tupla)
print(lista)
print(tupla)
print(nova_lista)

# verificando a existência de um elemento em uma tupla
lista = [1,2,3]
tupla = tuple(lista)
nova_lista = list(tupla)
print(4 in tupla)
print(4 not in tupla)   

# Observação: tupla é imutável e lista mutavel

# 4.2 Dicionários
carro = {'marca':'vw','modelo':'gol','ano':'2014','motor':'1.0'}
type(carro)

# Inserindo uma chave um valor em um dicionário existente
carro = {'marca':'vw','modelo':'gol','ano':'2014','motor':'1.0'}
carro['cor'] = 'azul'
print(carro)

carro['km'] = 280000
print(carro)

carro = {'marca':'vw','modelo':'gol','ano':'2014','motor':'1.0'}
'''
buscar um valor em um dicionário diretamente pela sua chave pode ser
um problema se por exemplo essa chave não existir no dicionário original
'''
carro['marca']

carro = {'marca':'vw','modelo':'gol','ano':'2014','motor':'1.0'}
'''
buscar um valor em um dicionário diretamente pela sua chave pode ser
um problema se por exemplo essa chave não existir no dicionário original
'''
carro['doc']

carro = {'marca':'vw','modelo':'gol','ano':'2014','motor':'1.0'}
'''
Alternativa
'''
carro.get('marca')

carro = {'marca':'vw','modelo':'gol','ano':'2014','motor':'1.0'}
'''
Alternativa
'''
carro.get('doc')
'''
Resumindo: para os dicionários o método get é bem semelhante à busca
diretamente pela chave, mas com uma importante diferença: pelo método
get, caso a chave não exista no dicionário original, ao onvés de travar o
programa, o método retorna vazio
'''

# Removendo o último para de chave e valor de um dicionário
carro = {'marca':'vw','modelo':'gol','ano':'2014','motor':'1.0'}
carro.popitem()

# Excluindo um item de um dicionário
carro = {'marca':'vw','modelo':'gol','ano':'2014','motor':'1.0'}
carro.pop('marca')
print(carro)

# deixando um dicionário sem elemento algum
carro = {'marca':'vw','modelo':'gol','ano':'2014','motor':'1.0'}
print(carro)
carro.clear()
print(carro)

# 4.4 Sets

# Criando conjuntos
nomes = {'Douglas', 'Daniela', 'Pedro', 'Maria'}
pesos = {78, 32, 86, 74}
print(nomes)
print(pesos)
print(type(nomes))

# impossibilidade de receber valores duplicados
alturas = {1.85, 1.34, 1.78, 1.69, 1.34}
print(alturas)

# Adição de elemento único em um conjunto
loja_a = {'garfo', 'faca', 'caneca', 'copo'}
loja_b = {'copo', 'caneca', 'taça', 'tigela'}
print(loja_a)
print(loja_b)
loja_a.add('prato')
loja_b.add('pote')
print(loja_a)
print(loja_b)

# Adição de mais de um elemento em um conjunto
loja_a.update(['bule', 'chaleira'])
print(loja_a)

# União de conjuntos
loja_c = loja_a.union(loja_b)
print(loja_c)

# Intersecção de conjuntos
loja_a = {'garfo', 'faca', 'caneca', 'copo'}
loja_b = {'copo', 'caneca', 'taça', 'tigela'}
interseccao = loja_a.intersection(loja_b)
print(interseccao)

# Verificando os elementos exclusivos na comparação de conjuntos
loja_a = {'garfo', 'faca', 'caneca', 'copo'}
loja_b = {'copo', 'caneca', 'taça', 'tigela'}
only_a = loja_a.difference(loja_b) 
only_b = loja_b.difference(loja_a)
print(only_a)
print(only_b)

# Excluindo elementos de um conjunto pelo método remove
loja_a = {'garfo', 'faca', 'caneca', 'copo'}
loja_b = {'copo', 'caneca', 'taça', 'tigela'}
loja_a.remove('faca')
print(loja_a)

'''
Esse método remove o elemento caso ele exista, caso não exista ele vai quebrar
'''

# Excluíndo elementos de um conjunto pelo método dicard
loja_a = {'garfo', 'faca', 'caneca', 'copo'}
loja_b = {'copo', 'caneca', 'taça', 'tigela'}
loja_a.discard('faca')
print(loja_a)

# Excluindo todos os elementos de um conjunto
loja_a = {'garfo', 'faca', 'caneca', 'copo'}
loja_a.clear()
print(loja_a)

'''
Agora imagine que você tem quatro possibilidades:
1ª Nota maior ou igual a 6: 'Parabéns você foi aprovado!'
2ª Nota menor que 6, mas maior ou igual a 4: 'Você deverá fazer uma prova de recuperação online'
3ª Nota menor 4, mas maio ou igual a 2: 'Você deverá fazer uma prova de recuperação presencial'
4ª Nota menor que 2:'Infelizmente você não foi aprovado dessa vez! continue tentando.'
'''
nota = float(input('Informe uma nota de 0 a 10: '))
if nota >= 6:
  print('Parabéns você foi aprovado!')
elif nota >= 4:
  print('Você deverá fazer uma prova de recuperação online')
elif nota >= 2:
  print('Você deverá fazer uma prova de recuperação presencial')
else:
  print('Infelizmente você não foi aprovado dessa vez! continue tentando.')