def le_valores():
    produto1 = int(input('Entre com o valor do primeiro produto: '))
    produto2 = int(input('Entre com o valor do segundo produto: '))
    produto3 = int(input('Entre com o valor do terceiro produto: '))
    lista = [produto1, produto2, produto3]
    return lista

def menor_preco(lista):
    menor = lista[0]
    for valor in lista:
        if valor < menor:
            menor = valor
    return menor

def qual_comprar():
    valores = le_valores()
    print('O produto a ser comprado é: ', menor_preco(valores))