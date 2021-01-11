num1 = float(input('Entre com o primeiro numero: '))
num2 = float(input('Entre com o segundo numero: '))
num3 = float(input('Entre com o terceiro numero: '))
num4 = float(input('Entre com o quarto numero: '))
num5 = float(input('Entre com o quinto numero: '))
lista = [num1, num2, num3, num4, num5]
soma = 0
contador = 0
for elemento in lista:
    soma = elemento + soma
    contador = contador + 1
print('A soma dos números é: ', soma)
print('A madia dos números é: ',soma / contador)
