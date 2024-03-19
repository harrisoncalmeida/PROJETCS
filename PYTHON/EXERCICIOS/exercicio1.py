#Exercício

print('Escolha o que deseja comprar:')
print('1 - maça')
print('2 - banana')
print('3 - laranja')
produto = int(input('Qual sua escolha?'))
qtd = int(input('Quantas unidades?'))
if (produto == 1):
    pagar = qtd * 2.3
    print('Você comprou {} maças. Total à pagar:' ' R$ ' '{} '.format(qtd, pagar))
else:
    if(produto == 2):
        pagar = qtd * 3.6
        print('Você comprou {} banana. Total à pagar:' ' R$ ' ' {}'.format(qtd, pagar))
    else:
        if(produto == 3):
            pagar = qtd * 1.85
            print('Você comprou {} laranja. Toral à pagar:' ' R$ ' '  {}'.format(qtd, pagar))
        else:
            print('Produto inexistente!')