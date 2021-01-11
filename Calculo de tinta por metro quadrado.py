def testa():
    print('Iniciando os testes')
    teste_pontual(15, 80)
    teste_pontual(55, 160)
    teste_pontual(109, 240)
    teste_pontual(216, 320)
    teste_pontual(272, 480)
    print('Testes finalizados.')

def teste_pontual (metros, valor_esperado):
    valor_calculado = quantoCusta(metros)
    if valor_calculado != valor_esperado:
        print('Valor errado para array' , metros)
        print('Valor esperado era', valor_esperado, 'mas recebeu:', valor_calculado)

def quantoCusta(metros):
    rendimento = 18 * 3
    if metros > rendimento:
        contador = 1
        while metros > rendimento:
            contador = contador + 1
            rendimento = rendimento + 54
        return contador * 80
    else:
        return 80