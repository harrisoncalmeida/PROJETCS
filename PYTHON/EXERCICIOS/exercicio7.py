#Erro colocando um caracter
x = int(input("Por favor digite um número: "))

#Resolução até colocar o número
while True:
    try:
        x = int(input("Por favor digite um número:"))
        break
    except ValueError:
        print("Oops! Número inválido. Tente novamente...")

#Resolução com divisão de 0
def div():
    try:
        num1 = int(input("Digite um número: "))
        num2 = int(input("Digite um número: "))
        res = num1 / num2
    except ZeroDivisionError:
        print("Oops! Erro de divisão por zero...")
    except:
        print("Algo de errado aconteceu...")
    else:
        return res
    finally:
        print("Executará sempre!")

#Programa principal
print(div())