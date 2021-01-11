base = int(input('Entre com a base: '))
expoente = int(input('Entre com o expoente: '))
produto = 1
for numero in range(1, expoente + 1):
    produto = base * produto
    print(produto)