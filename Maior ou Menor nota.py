def maior_nota(lista):
    maior = lista[0]
    for notas in lista:
        if notas > maior:
            maior = notas
    return maior

def menor_nota(lista):
    menor = lista[0]
    for notas in lista:
        if notas < menor:
            menor = notas
    return menor

def le_notas():
    num = int(input('Entre com a primeira nota (para finalizar entre com -1: '))
    lista = [num]
    while num != -1:
        lista.append(num)
        num = int(input('Entre com a próxima nota (para finalizar entre com -1: '))
    return lista

def qual_as_notas():
    valores = le_notas()
    print('A maior nota é: ', maior_nota(valores))
    print('A menor nota é: ', menor_nota(valores))