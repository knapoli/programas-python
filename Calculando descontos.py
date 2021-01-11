valor = float(input("Qual o preço do produto? R$ "))
desconto = valor - (valor /100)*5
novoValor = valor - desconto
print("O produto custava R${}, na promoção com desconto de 5% vai custarR${:.2f}".format(valor, desconto))