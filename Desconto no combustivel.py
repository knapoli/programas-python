tipoCombustivel = input('Entre com (a) para alcool e (g) para gasolina: ')
litros = float(input('Entre com a quantidade em litros: '))
alcool = float(1.90)
gasolina = float(2.50)

if tipoCombustivel == 'a':  # se o combustivel for alcool
    if litros <= 20:
        valorTotal = (litros * alcool)
        desconto = valorTotal / 100 * 3
        valorFinal = valorTotal - desconto
        print('Valor a pagar R$', valorFinal)
    if litros > 20:
        valorTotal = (litros * alcool)
        desconto = valorTotal / 100 * 5
        valorFinal = valorTotal - desconto
        print('Valor a pagar R$', valorFinal)

if tipoCombustivel == 'g':  # se o combustivel for gasolina
    if litros <= 20:
        valorTotal = (litros * gasolina)
        desconto = valorTotal / 100 * 4
        valorFinal = valorTotal - desconto
        print('Valor a pagar R$', valorFinal)
    if litros > 20:
        valorTotal = (litros * gasolina)
        desconto = valorTotal / 100 * 6
        valorFinal = valorTotal - desconto
        print('Valor a pagar R$', valorFinal)