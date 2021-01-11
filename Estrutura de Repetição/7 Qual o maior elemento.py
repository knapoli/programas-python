num1 = float(input('Entre com o primeiro numero: '))
num2 = float(input('Entre com o segundo numero: '))
num3 = float(input('Entre com o terceiro numero: '))
num4 = float(input('Entre com o quarto numero: '))
num5 = float(input('Entre com o quinto numero: '))
lista = [num1, num2, num3, num4, num5]
primeiraVez = True
for elemento in lista:
    if primeiraVez == True:
        maiorElemento = elemento
        primeiraVez = False
    if elemento > maiorElemento:
        maiorElemento = elemento
print('O maior elemento é: ',maiorElemento)
