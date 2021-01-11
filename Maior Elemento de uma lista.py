def maior_elemento (lista):
    primeiraVez = True
    maiorElemento = 0
    for item in lista:
        if primeiraVez == True:
            maiorElemento = item
            primeiraVez = False
        if item > maiorElemento:
            maiorElemento = item
    return(maiorElemento)


