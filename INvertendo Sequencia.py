teclado = int(input('Entre com um número inteiro diferente de 0:'))

numeros = []
while teclado != 0:
    numeros.append (teclado)
    teclado = int(input('Entre com um número inteiro diferente de 0:'))

tamanho = len(numeros)
tamanho = tamanho - 1

while tamanho >= 0:
    print(numeros[tamanho])
    numeros[tamanho] = numeros[tamanho] - 1
    tamanho = tamanho - 1
