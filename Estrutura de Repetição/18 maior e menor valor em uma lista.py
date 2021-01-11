def maior_e_maior_elemento():
    lista = []
    verificador = True
    while verificador == True:
        numero = float(input('Entre com o numero (Digite 00 para retornar os valores): '))
        if numero == 00:
            verificador = False
        else:
            lista.append(numero)
    maior = encontra_maior(lista)
    menor = encontra_menor(lista)
    print('O maior valor da lista é: ', maior)
    print('O menor valor da lista é: ', menor)
    print('A soma dos valores é: ', maior + menor)

def encontra_maior(lista):
    primeiraVez = True
    maiorElemento = 0
    for item in lista:
        if primeiraVez == True:
            maiorElemento = item
            primeiraVez = False
        if item > maiorElemento:
            maiorElemento = item
    return (maiorElemento)

def encontra_menor(lista):
    primeiraVez = True
    menorElemento = 0
    for item in lista:
        if primeiraVez == True:
            menorElemento = item
            primeiraVez = False
        if item < menorElemento:
            menorElemento = item
    return (menorElemento)