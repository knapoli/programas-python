pesoMorango = float(input('Entre com kg do morango: '))
pesoMaca = float(input('Entre com kg da maça: '))

if pesoMorango < 5:
    valorMorango = float(2.50)
else:
    valorMorango = float(2.20)

if pesoMaca < 5:
    valorMaca = float(1.80)
else:
    valorMaca = float(1.50)

valorTotal = (pesoMorango * valorMorango) + (pesoMaca * valorMaca)
pesoTotal = pesoMorango + pesoMaca
if pesoTotal > 8 or valorTotal > 25:
    desconto = valorTotal / 100 * 10
    valorFinal = valorTotal - desconto
    print('Valor a ser pago: ', valorFinal)
else:
    print('Valor a ser pago: ', valorTotal)