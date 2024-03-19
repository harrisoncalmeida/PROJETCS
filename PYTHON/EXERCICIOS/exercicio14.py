# not

#x = True
#y = False
#print(not x)
#print(not y)

# and

#x = False
#y = True
#print(x and y)

# or

#x = True
#y = False
#print(x or y)

#Espressões lógicas

#x = 10
#y = 1
#res = not x > y
#print(res)

#x = 10
#y = 1
#z = 5.5
#res = x > y and z == y
#print(res)

#Exercício

m1 = float(input('Digite a nota da 1° matéria'))
m2 = float(input('Digite a nota da 2º matéria'))
m3 = float(input('Digite a nota da 3º matéria'))
if m1 >= 7 and m2 >= 7 and m3 >= 7:
    print('O aluno está aprovado de ano!')
else:
    print('O aluno não passou de ano!')