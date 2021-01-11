largura = int(input('Digite a largura: '))
altura = int(input('Digite a altura: '))
linha = 1
coluna =1

while linha <= altura:
    while coluna <= largura:
        if linha == 1 or coluna == 1 or linha == altura or coluna == largura:
            print ('#', end = '')
            print ('linha: ',linha,':', coluna)
        else:
            print(' ', end = '')
        coluna = coluna + 1
        print()
    linha = linha + 1
