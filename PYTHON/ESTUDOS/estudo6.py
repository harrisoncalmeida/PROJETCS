x = 1
while(x <= 10):
    print(x)
    x = x + 1

# Outro exemplo

inicial = int(input("Qual valor deseja iniciar a contagem?"))
final = int(input("Qual valor deseja encerrar a contagem?"))
x = inicial
while (x <= final):
    if (x % 2 == 0):
        print(x)
    x = x + 1

#Exemplo de acumulador

soma = 0
cont = 1
while (cont <=5):
    x = float(input("Digite a {}ª nota:".format(cont)))
    soma = soma + x
    cont = cont + 1
media = soma / 5
print("Média final: {}".format(media))

#Exemplo especiais de atribuição

soma = 0
cont = 1
while (cont <= 5):
    x = int(input("Digite o {}ª número".format(cont)))
    soma += x  # Equivalente: soma = soma + x
    cont += 1  # Equivalente: cont = cont + 1
print("Somatório: {}".format(soma))

#Exemplo validando a entrada
x = int(input("Digite um valor maior do que zero: "))
while (x <=0):
    x = int(input("Digite um valor maior do que zero:"))
print("Você digitou {}. Encerrando o programa...".format(x))

#Exemplo de break
print("Digite uma mensagem que irei repetir para você!")
print("Para encerrar escreva 'sair'. ")
while True:
    texto = input("")
    print(texto)
    if texto == 'sair':
        break
    print("Encerrando programa...")

#Exemplo de coninue
nome = input("Digite o seu nome?")
if (nome != "Lenhadorzinho"):
    continue

senha = input("Qual a sua senha?")
if (senha == "Inkinoz"):
    break

print("Acesso concedido.")

#Exemplo "Truthy" e "Falsey"
nome = ""
while not nome:
    nome = input("Digite o seu nome:")
valor = int(input("Digite qualquer número:"))
if valor:
    print("Você digitou um valor diferente de zero.")
else:
    print("Você difgitou zero.")