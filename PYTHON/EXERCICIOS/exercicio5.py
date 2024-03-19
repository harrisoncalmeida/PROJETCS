#Escopo de variáveis
def comida():
    print(ovos)

#Programa principal
ovos = 12
comida()

def comid():
    ovos = 12
    bacon()
    print(ovos)

def bacon():
    ovos = 6

comida()

def comida():
    ovos = "variável local de comida"
    print(ovos)

def bacon ():
    ovos = "variável local de bacon"
    print(ovos)
    comida()
    print(ovos)

ovos = "variável global"
bacon()
print(ovos)

#Instrução global
def comida():
    global ovos
    ovos = "comida"

ovos = "global"
comida()
print(ovos)