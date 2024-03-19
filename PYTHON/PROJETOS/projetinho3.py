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
    if sabor != "tr" and sabor != "TR" and sabor != "pr" and sabor != "PR" and sabor != "es" and sabor != "ES":
        print("Opção inválida. Você está digitando o sabor errado, digite apenas (tr/pr/es). ")
        continue  # Se usuário digitar algo inválido, voltar para o começo do while

    quantidade = input("Digite a quantidade de bolas de sorvete (1/2/3): ")
    if quantidade != "1" not in quantidade != "2" not in quantidade != "3":
        print("Opção inválida. Você está digitando a quantidade errada, digite apenas (1/2/3). ")
        continue  # Se usuário digitar algo inválido, voltar para o começo do while

    if quantidade == "1" and sabor == "tr":
        print(f"Você pediu {quantidade}. bola de sorvete no sabor TRADICIONAL: R$ 6,00")
        acumulador = acumulador + 6.00  # Pegue o valor que tinha no acumulador e some com 6.00





