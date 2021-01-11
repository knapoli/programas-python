def soma_elementos (lista):
    tamanho = len(lista)
    tamanho = tamanho - 1
    guardar = 0
    while tamanho >= 0:
        primeiroItem = lista[0]
        guardar = primeiroItem + guardar
        del lista[0]
        tamanho = tamanho - 1
    return (guardar)