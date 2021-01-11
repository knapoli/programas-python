n = int(input('Insira a quantidade de linhas: '))
m = int(input('Insira a quantidade de colunas: '))

linha = 1
coluna = 1

while linha <= n:
    while coluna <= m:
        if coluna == 1 or linha == 1 or coluna == m or linha == n:
            print('#', end='\t')
        else:
            print(' ', end = '\t' )
        coluna = coluna + 1
    linha = linha + 1
    print()
    coluna = 1