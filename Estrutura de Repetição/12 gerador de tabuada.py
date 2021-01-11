numerador = int(input('Entre com o numero da tabuada que deseja: '))
for multiplicador in range(1, 11):
    produto = numerador * multiplicador
    print(numerador, 'x', multiplicador, '=', produto)