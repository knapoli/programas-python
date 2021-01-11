def MinMax(temperaturas):
    print('A menor temperatura do mês foi: ', minima(temperaturas), 'C')
    print('A maior temperatura do mês foi: ', maxima(temperaturas), 'C')

def minima(temps):
    min = temps[0]
    i = 1
    while i < len(temps):
        if temps[i] < min:
            min = temps[i]
        i = i + 1
    return min

def testa_minima():
    print('Iniciando os testes')
    teste_pontual([0], 0)
    teste_pontual([0, 0, 0, 0, 0],0)
    teste_pontual([1, 2, 3, 4, 5, 6, 7, 8, 9], 1)
    teste_pontual([-15, -22, -5, 20], -22)
    print('Finalizando testes')

def teste_pontual(temp, valor_esperado):
    valor_calculado = minima(temp)
    if valor_calculado != valor_esperado:
        print('valor errado para array', temp)
        print('Valor esperado: ', valor_esperado, 'Valor calculado: ', valor_calculado)