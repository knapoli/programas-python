import math
numeroMax = int(input('Entre com o numero: '))
lista = []
for i in range(2, numeroMax + 1):
    lista.append(i)


i = int(0)
numeroVerificar = lista[i]

while numeroVerificar < numeroMax:
    contador = 2
    quantidadeDivisoes = 0
    multiplicacaoElemento = numeroVerificar * contador
    while multiplicacaoElemento <= numeroMax:
        if multiplicacaoElemento in lista:
            lista.remove(multiplicacaoElemento)
            quantidadeDivisoes = quantidadeDivisoes + 1
        contador = contador + 1
        multiplicacaoElemento = numeroVerificar * contador

    i = i + 1
    numeroVerificar = lista[i]
print(lista)
print(quantidadeDivisoes)
