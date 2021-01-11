max = int(input("entre com a quantidade de linhas "))
linha = 1
numero = 1
while linha <= max:
    posicao = 1
    while posicao <= linha:
        print(numero, end=' ')
        numero += 1
        posicao += 1
        
    linha += 1
    print()