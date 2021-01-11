numero = int(1)
numeroInicial = numero
soma = numero
primeiraVez = True
while numero <= 16:
    if primeiraVez == True:
        numero = int(input('Entre com um numero inteiro para saber seu fatorial: '))
        numeroInicial = numero
        primeiraVez = False
    if numero <=16:
        if numero == 0:
            print('0 ! = 1')
        else:
            while numero > 1:
                proximo = numero - 1
                soma = soma * proximo
                numero = proximo
            print(numeroInicial,'! =', soma)
        numero = int(input('Entre com um numero inteiro para saber seu fatorial: '))
        while numero < 0 or numero > 16:
            numero = int(input('Número invalido. Entre com um numero inteiro para saber seu fatorial: '))
            soma = numero
            numeroInicial = numero
        soma = numero
        numeroInicial = numero
    else:
        while numero < 0 or numero > 16:
            numero = int(input('Número invalido. Entre com um numero inteiro para saber seu fatorial: '))
            numeroInicial = numero