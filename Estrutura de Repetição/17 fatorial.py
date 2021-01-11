numero = int(input('Entre com um numero inteiro para saber seu fatorial: '))
numeroInicial = numero
soma = numero
if numero == 0:
    print('0 ! = 1')
else:
    while numero > 1:
        proximo = numero - 1
        soma = soma * proximo
        numero = proximo
    print(numeroInicial,'! =', soma)