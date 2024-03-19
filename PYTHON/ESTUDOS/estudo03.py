# Solicita ao usuário que insira a primeira nota
nota1 = float(input("Por favor, insira a primeira nota: "))

# Verifica se a nota está no intervalo correto (0 a 10)
while nota1 < 0 or nota1 > 10:
  print("Erro! A nota deve estar no intervalo de 0 a 10. ")
  nota1 = float(input("Por favor, insira a primeira nota novamente: "))

# Solicita ao usuário que insira a segunda nota
nota2 = float(input("Por favor, insira a segunda nota: "))

# Verifica se a nota está no intervalo correto (0 a 10)
while nota2 < 0 or nota2 > 10:
  print("Erro! A nota deve estar no intervalo de 0 a 10. ")
  nota2 = float(input("Por favor, insira a segunda nota novamente. "))

# Solicita ao usuário que insira a terceira nota
nota3 = float(input("Por favor, insira a terceira nota: "))

# Verifica se a nota está no intervalo correto (0 a 10)
while nota3 < 0 or nota3 > 10:
  print("Erro! A nota deve estar no intervalo de 0 a 10 ")
  nota3 = float(input("Por favor, insira a terceira nota novamente: "))

# Média final do aluno
nota_total = ((nota1 + nota2 + nota3) / 3)
print("Média final do aluno: {}".format(nota_total))

# Verifica se o aluno foi aprovado ou reprovado
if nota_total >= 7:
  print("Parabéns! Você está aprovado. ")
else:
  print("Você está reprovado.")