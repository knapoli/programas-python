contador = 1
lista = []
par = 0
impar = 0
while contador <=10:
    numero = int(input('Entre com um numero: '))
    if numero % 2 == 0:
        par = par + 1
    if numero % 2 == 1:
        impar = impar + 1
    contador = contador + 1

print('par', par)
print('impar', impar)