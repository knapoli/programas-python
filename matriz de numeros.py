coluna = int(input('Entre com o numero de colunas '))
contaColunas = 1
numero = 1
linha = int(input('Entre com o numero de linhas '))
contaLinha = 1
while contaLinha <= linha:
    while contaColunas <= coluna:
        print (numero, end=' ')
        numero += 1
        contaColunas += 1
    contaLinha += 1
    contaColunas = 1
    print()
    