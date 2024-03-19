# Mensagem de boas_vindas
print("Seja bem vindo a sorveteria do William Harrison Correia de Almeida")
print("-------------------------------------Cardápio-------------------------------------")
print("| Nº de bolas | Sabor Tradiconal (tr) | Sabor Premium (pr) | Sabor Especial (es) |")
print("|      1      |       R$ 6,00         |      R$ 7,00       |        R$ 8,00      |")
print("|      2      |       R$ 10,00        |      R$ 12,00      |        R$ 14,00     |")
print("|      3      |       R$ 14,00        |      R$ 17,00      |        R$ 20,00     |")
print("----------------------------------------------------------------------------------")

acumulador = 0

while True:
    # Entrada de dados
    sabor = input("\nDigite o sabor do sorvete (tr/pr/es): ")
    sabor + sabor.upper()
    if sabor != "tr" and sabor != "TR" and sabor != "pr" and sabor != "PR" and sabor != "es" and sabor != "ES":
        print("Opção inválida. Você está digitando o sabor errado, digite apenas (tr/pr/es). ")
        continue  # Se usuário digitar algo inválido, voltar para o começo do while

    quantidade = input("Digite a quantidade de bolas de sorvete (1/2/3): ")
    if quantidade != "1" not in quantidade != "2" not in quantidade != "3":
        print("Opção inválida. Você está digitando a quantidade errada, digite apenas (1/2/3). ")
        continue  # Se usuário digitar algo inválido, voltar para o começo do while
        # Sabores Tradicionais
    if quantidade == "1" and sabor == "tr":
        print(f"Você pediu {quantidade} bola(s) de sorvete no sabor TRADICIONAL: R$ 6,00")
        acumulador = acumulador + 6.00  # Pegue o valor que tinha no acumulador e some com 6.00
    elif quantidade == "2" and sabor == "tr":
        print(f"Você pediu {quantidade} bola(s) de sorvete no sabor TRADICIONAL: R$ 10,00")
        acumulador = acumulador + 10.00  # Pegue o valor que tinha no acumulador e some com 10.00
    elif quantidade == "3" and sabor == "tr":
        print(f"Você pediu {quantidade} bola(s) de sorvete no sabor TRADICIONAL: R$ 14,00")
        acumulador = acumulador + 14.00  # Pegue o valor que tinha no acumulador e some com 14.00
        #Sabores Premium
    elif quantidade == "1" and sabor == "pr":
        print(f"Você pediu {quantidade} bola(s) de sorvete no sabor PREMIUM: R$ 7,00")
        acumulador = acumulador + 7.00  # Pegue o valor que tinha no acumulador e some com 7.00
    elif quantidade == "2" and sabor == "pr":
        print(f"Você pediu {quantidade} bola(s) de sorvete no sabor PREMIUM: R$ 12,00")
        acumulador = acumulador + 12.00  # Pegue o valor que tinha no acumulador e some com 12.00
    elif quantidade == "3" and sabor == "pr":
        print(f"Você pediu {quantidade} bola(s) de sorvete no sabor PRMEIUM: R$ 17,00")
        acumulador = acumulador + 17.00  # Pegue o valor que tinha no acumulador e some com 17.00
        #Sabores Especiais
    elif quantidade == "1" and sabor == "es":
        print(f"Você pediu {quantidade} bola(s) de sorvete no sabor PRMEIUM: R$ 8,00")
        acumulador = acumulador + 8.00  # Pegue o valor que tinha no acumulador e some com 8.00
    elif quantidade == "2" and sabor == "es":
        print(f"Você pediu {quantidade} bola(s) de sorvete no sabor PRMEIUM: R$ 14,00")
        acumulador = acumulador + 14.00  # Pegue o valor que tinha no acumulador e some com 14.00
    elif quantidade == "3" and sabor == "es":
        print(f"Você pediu {quantidade} bola(s) de sorvete no sabor PRMEIUM: R$ 20,00")
        acumulador = acumulador + 20.00  # Pegue o valor que tinha no acumulador e some com 20.00

    # Pergunta se o cliente deseja pedir mais
    pedir_mais = input("Deseja mais algum sorvete (Digite: s/n)?: ")
    pedir_mais = pedir_mais.upper()  # Resolvo o problema de digitar "s" e "S"
    if pedir_mais == "S":
      continue
    else:
      print("O valor total a ser pago: R${:.2f}".format(acumulador))
      break