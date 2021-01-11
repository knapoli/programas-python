numerador = int(input('Entre com qual tabuada que voce quer: '))
contador = 1
while numerador > 0:
    while contador <= 10:
        produto = numerador * contador
        print(numerador,'x',contador,'=',produto)
        contador = contador + 1
    numerador = int(input('Entre com qual tabuada que voce quer: '))
    contador = 1