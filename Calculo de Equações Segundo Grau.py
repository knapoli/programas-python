def pega_raizes():
    import math
    valorA = float(input('Entre com o valor de a: '))
    if valorA == 0:
        print ('Não é uma equação de segundo grau')
    if valorA != 0:
        valorB = float(input('Entre com o valor de b: '))
        valorC = float(input('Entre com o valor de c: '))
        delta = (valorB) * (valorB) - (4 * valorA * valorC)
        raizDelta = math.sqrt(delta)
        if delta < 0:
            print('Delta negativo, equação não possui raizes reais.')
        if delta == 0:
            print((-(valorB))/(2 * valorA))
        if delta > 0:
            print(((-(valorB)) + raizDelta) / (2 * valorA))
            print(((-(valorB)) - raizDelta) / (2 * valorA))

