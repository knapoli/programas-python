def MinMax (temperaturas):
    print ('A menor temperatura do mes foi: ', minima(temperaturas), 'C')
    print('A maior temperatura do mes foi: ', maxima(temperaturas), 'C')

def minima(temp):
    min = temp[0]
    i = 1
    while i < len(temp):
        if temp[i] < min:
            min = temp[i]
        i = i + 1
    return min


def maxima(temp):
    max = temp[0]
    i = 1
    while i < len(temp):
        if temp[i] > max:
            max = temp[i]
        i = i + 1
    return max

def testa_minima():
    print('Iniciando os testes.')
    teste_pontual ([0,0,0,0,0,0],0)
    teste_pontual([1, 2, 3, 4, 5, 6, 7, 8, 9], 9)
    teste_pontual([2, 5, 6, -55, -66, 30, 55], 55)
    teste_pontual([-22, -520, 98, 55, 0], 98)
    teste_pontual([-22, -99, -45, -23, -1], -1)

    print('Finalizando os testes.')

    
def teste_pontual(lista_temperaturas, valor_esperado):
    valor_calculado = maxima(lista_temperaturas)
    if valor calculado =! valor_esperado:
        print('Valor errado para array: ', lista_temperaturas)
        print('Valor calculado foi de: ', valor_calculado, 'porem o valor esperado era de: ', valor_esperado)
