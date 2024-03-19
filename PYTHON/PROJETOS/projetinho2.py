# Início das variáveis globais
lista_colaborador = []
id_colaborador = 0

# Função para cadastrar um novo colaborador
def cadastrar_colaborador(id):
  print("*********************************************************************************")
  print("-------------------------- MENU CADASTRAR COLABORADOR ---------------------------")
  print("Id do colaborador {}".format(id))
  nome = input("Por favor entre com o nome: ")
  setor = input("Por favor entre com o setor: ")
  salario = int(input("Por favor entre com o pagamento: R$ "))
  dicionario_colaborador = {"id": id,
                            "nome" : nome,
                            "setor" : setor,
                            "salario" : salario}
  lista_colaborador.append(dicionario_colaborador.copy())
  print("*********************************************************************************")
  print("-------------------------------- MENU PRINCIPAL ---------------------------------")
# Fim de cadastrar um colaborador

# Função para consultar um colaborador
def consultar_colaborador():
  print("*********************************************************************************")
  print("-------------------------- MENU CONSULTAR COLABORADOR ---------------------------")
  while True:
    opcao_consultar = input("Escolha a opção desejada: \n" +
                          "1 - Consultar todos os colaboradores \n" +
                          "2 - Consultar colaborador por id \n" +
                          "3 - Consultar Colaborador por setor \n" +
                          "4 - Retornar \n"
                          ">>")
    if opcao_consultar == "1":
      for colaborador in lista_colaborador: # colaborador vai varrer toda a lista de colaborador
        print("--------------------------------------")
        for key, value in colaborador.items(): # varrer todos os conjuntos chave e valor do dicionario colaborador
          print("{}: {}".format(key, value))
        print("--------------------------------------")
    elif opcao_consultar == "2":
      valor_desejado = int(input("Entre com o ID do colaborador: "))
      for colaborador in lista_colaborador:
        if colaborador["id"] == valor_desejado:
          print("--------------------------------------")
          for key, value in colaborador.items():
            print("{}: {}".format(key, value))
          print("--------------------------------------")
    elif opcao_consultar == "3":
      valor_desejado = input("Entre com o Setor do colaborador: ")
      for colaborador in lista_colaborador:
        if colaborador["setor"] == valor_desejado:
          print("--------------------------------------")
          for key, value in colaborador.items():
            print("{}: {}".format(key, value))
          print("--------------------------------------")
    elif opcao_consultar == "4":
      return # Sai da função consultar e volta para o principal
    else:
      print("Opção inválida. Tente novamente.")
      continue  # Volta para o início do laço
# Fim de consultar um colaborador

# Função para remover um colaborador
def remover_colaborador():
  print("*********************************************************************************")
  print("--------------------------- MENU REMOVER COLABORADOR ----------------------------")
  valor_desejado = int(input("Entre o ID do colaborador a ser removido: "))
  for id in lista_colaborador:
    if id["id"] == valor_desejado:
      lista_colaborador.remove(id)
      print("Colaborador Removido.")
  print("*********************************************************************************")
  print("-------------------------------- MENU PRINCIPAL ---------------------------------")
# Fim de remover um colaborador

# Início da Função
print("Bem-vindo ao Controle de Colaboradores do William Harrison Correia de Almeida.")
print("*********************************************************************************")
print("-------------------------------- MENU PRINCIPAL ---------------------------------")
while True:
  opcao_principal = input("Escolha a opção desejada: \n" +
                          "1 - Cadastar Colaborador \n" +
                          "2 - Consultar Colaborador(es) \n" +
                          "3 - Remover Colaborador \n" +
                          "4 - Sair \n"
                          ">>")
  if opcao_principal == "1":
    id_colaborador = id_colaborador + 1
    cadastrar_colaborador(id_colaborador)
  elif opcao_principal == "2":
    consultar_colaborador()
  elif opcao_principal == "3":
    remover_colaborador()
  elif opcao_principal == "4":
    break # Encerra o laço principal

  else:
    print("Opção inválida. Tente novamente.")
    continue # Volta para o início do laço
# Fim de Função