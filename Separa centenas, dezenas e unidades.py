numero = int(input('Entre com um numero inteiro menor que 1000: '))

if numero < 1000 and numero > 0:
    unidade = numero % 10
    numero = (numero - unidade) / 10
    dezena = numero % 10
    numero = (numero - dezena) / 10
    centena = numero % 10
    dezena = int(dezena)
    centena = int(centena)

    if centena >= 1:
        if centana == 1:
            print(centena, 'centena', dezena, 'dezena e', unidade, 'unidade')
        if centena > 1:
            print(centenas, 'centena', dezena, 'dezena e', unidade, 'unidade')
    if centana < 0 and dezena > 0:
        print

else:
    print('Número inválido.')