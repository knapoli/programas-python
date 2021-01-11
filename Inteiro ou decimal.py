numero = float(input('Entre com o numeral: '))

if (numero // 1) == numero:
    print('É inteiro')
else:
    print('É decimal, valor arredondado:', round(numero))