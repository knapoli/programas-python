contador = 0
pergunta1 = input('Telefonou para a vítima? ')
if pergunta1 == 's':
    contador = contador + 1

pergunta2 = input('Esteve no local do crime? ')
if pergunta2 == 's':
    contador = contador + 1

pergunta3 = input('Mora perto da vítima? ')
if pergunta3 == 's':
    contador = contador + 1

pergunta4 = input('Devia para a vítima? ')
if pergunta4 == 's':
    contador = contador + 1

pergunta5 = input('Já trabalhou com a vítima? ')
if pergunta5 == 's':
    contador = contador + 1

if contador < 2:
    print('Inocente')
if contador == 2:
    print('Suspeita')
if contador == 3 or contador == 4:
    print('Cúmplice')
if contador ==5:
    print('Assassino')