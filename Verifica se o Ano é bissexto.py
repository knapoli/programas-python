def verifica_ano_bissexto():
    ano = int(input('Entre com o ano a ser verificado: '))
    restoDivisaoPorQuatro = ano % 4
    restoDivisaoPorCem = ano % 100
    restoDivisaoPorQuatrocentos = ano % 400
    if restoDivisaoPorQuatro == 0:
        if restoDivisaoPorCem == 0 and restoDivisaoPorQuatrocentos != 0:
            print('Não é bissexto')
        else:
            print('É bissexto')
    else:
        print('Não é bissexto')