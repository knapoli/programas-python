valor = float(input('Qual valor do saque? '))
if valor >= 10 and valor <= 600:
    unidade = valor % 10
    unidadeGuardada = int(unidade)
    valor = (valor - unidade) / 10
    dezena = valor % 10
    dezena = int(dezena)
    valor = (valor - dezena) / 10
    centena = valor % 10
    centena = int(centena)

    if centena > 0:
        if centena == 1:
            print (centena, 'nota de 100')
        else:
            print (centena, 'notas de 100')
    if dezena > 0:
        if dezena < 5:
            if dezena == 1:
                print(dezena, 'nota de 10')
            else:
                print (dezena, 'notas de 10')
        if dezena == 5:
            print('1 nota de 50')
        if dezena > 5:
            print ('1 nota de 50')
            dezena = dezena - 5
            if dezena > 1:
                print (dezena, 'notas de 10')
            else:
                print('1 nota de 10')
    if unidadeGuardada > 0:
        if unidadeGuardada < 5:
            if unidadeGuardada == 1:
                print('1 nota de 1')
            else:
                print(unidadeGuardada, 'notas de 1')
        if unidadeGuardada == 5:
            print('1 nota de 5')
        if unidadeGuardada > 5:
            print ('1 nota de 5')
            unidadeGuardada = unidadeGuardada - 5
            if unidadeGuardada > 1:
                print (unidadeGuardada, 'notas de 1')
            else:
                print('1 nota de 1')

else:
    print ('valor invalido, entre com um valor entre 10 e 600')
