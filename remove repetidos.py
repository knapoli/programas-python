def remove_repetidos (lista):
    tamanho = len(lista)
    tamanho = tamanho - 1
    listaIntermediaria = []
    while tamanho >= 0:
        primeiroItem = lista[0]
        if primeiroItem in listaIntermediaria:
            del lista[0]
        else:
            guardar = [primeiroItem]
            listaIntermediaria = listaIntermediaria + [primeiroItem]
            del lista[0]
        tamanho = tamanho - 1
    listaIntermediaria.sort()
    return(listaIntermediaria)
