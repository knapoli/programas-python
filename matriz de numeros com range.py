coluna = int(input('Entre com a quantidade de colunas '))
contador = 0
linha = int(input('Entre com a quantidade de linhas '))
for i in range (1, linha + 1):
    for i in range (1, coluna + 1):
        contador += 1
        print(contador, end=' ')
    print()