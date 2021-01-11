tipoCarne = input('Entre com o tipo de carne, (f) para filé duplo, (a) para alcatra e (p) para picanha: ')
quantidade = float(input('Entre com a quantidade de carne em kg: '))
pagamento = input('Entre com (d) para dinheiro e (c) para pagar com o cartao tabajara ')

if tipoCarne == 'f':
    tipoCarne = 'File Duplo'
    if quantidade <= 5:
        valor = float(4.90)
    else:
        valor = float(5.80)

if tipoCarne == 'a':
    tipoCarne = 'Alcatra'
    if quantidade <= 5:
        valor = float(5.90)
    else:
        valor = float(6.80)

if tipoCarne == 'p':
    tipoCarne = 'Picanha'
    if quantidade <= 5:
        valor = float(6.90)
    else:
        valor = float(7.80)

valorTotal = valor * quantidade

if pagamento == 'c':
    pagamento = 'Cartao Tabajara'
    desconto = valorTotal / 100 * 5
if pagamento == 'd':
    pagamento = 'Dinheiro'
    desconto = 0

print('Cupom fiscal')
print(tipoCarne)
print(quantidade,'kg')
print('Valor total R$',valorTotal)
print('Pagamento no', pagamento)
if desconto > 0:
    print('Valor desconto: R$ %.2f'%(desconto))
print('Total a pagar: R$ %.2f'%(valorTotal - desconto))