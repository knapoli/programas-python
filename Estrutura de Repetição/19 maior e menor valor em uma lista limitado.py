def maior_e_menor_elemento():
    lista = []
    numero = float(1)
    while numero >=0 and numero <= 1000:
        numero = float(input('Entre com o numero: '))
        if numero >=0 and numero <= 1000:
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