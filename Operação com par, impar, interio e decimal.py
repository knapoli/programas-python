numero1 = float(input('Entre com o primeiro numero: '))
numero2 = float(input('Entre com o segundo numero: '))
operação = input('Entre com o 1 para soma, 2 para subtração, 3 para multiplicação e 4 para divisão: ')

if operação == '1':
    resultado = numero1 + numero2
if operação == '2':
    resultado = numero1 - numero2
if operação == '3':
    resultado = numero1 * numero2
if operação == '4':
    resultado = numero1 / numero2
print(resultado, ' Resultado da operação.')

resto = resultado % 2
operação = float(operação)

if resto == 0:
    print('É par')
if resto == 1:
    print('É impar')

if (resultado // 1) == resultado:
    print('É inteiro')
else:
    print('É decimal')

if resultado > 0:
    print('Positivo')
else:
    print('Negativo')
