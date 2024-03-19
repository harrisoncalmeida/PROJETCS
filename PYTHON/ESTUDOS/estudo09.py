#Função de execução def realce()
def realce():
    #corpo da função
    print("|", "_" * 10, "|")
    print("|", "_" * 10, "|")

realce()
print("     MENU")
realce()

#Parâmentros em funções
def realce(s1):
    print("|", "_" * 10, "|")
    print("|", "_" * 10, "|")
    print(s1)
    print("|", "_" * 10, "|")
    print("|", "_" * 10, "|")

realce("     Menu")

def sub2(x, y):
    res = x - y
    print(res)

sub2(5, 7)
sub2(7,5)
sub2(y = 7, x = 5)

def soma3(x, y, z):
    res = x + y + z
    print(res)

def soma3(x = 0, y = 0, z = 0):
    res = x +y + z
    print(res)

soma3(1,2,3)
soma3(1,2)  #z foi omitido
soma3(1)  #y e z foram omitido
soma3()  #x, y e z foram omitdo

#Exercicio 1
def borda(s1):
    tam = len(s1)
    # só imprime caso exista algum caractere
    if tam:
        print("+","-" * tam,"+")
        print("|",s1, "|")
        print("+", "-" * tam, "+")

borda("Olá, mundo!")
borda("Lógica de programação e algoritmos")
