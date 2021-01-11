def e_triangulo():
    lado1 = int(input('Entre com o lado 1: '))
    lado2 = int(input('Entre com o lado 2: '))
    lado3 = int(input('Entre com o lado 3: '))
    if lado1 + lado2 >= lado3 and lado1 + lado3 >= lado2 and lado2 + lado3 >= lado1:
        print('É triangulo.')
        if lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
            print('É triangulo Escaleno')
        elif lado1 == lado2 and lado1 == lado3 and lado2 == lado3:
            print('É triangulo Equilátero')
        elif lado1 == lado2 and lado1 != lado3 or lado1 == lado3 and lado1 != lado2 or lado1 != lado2 and lado1 != lado3:
            print('É triangulo Isósceles.')

    else:
        print('Não é triangulo.')
