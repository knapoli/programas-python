salario = float(input("Qual é o salario do funcionário? R$ "))
aumento = salario + (salario /100)*15
print("O produto custava R${}, na promoção com desconto de 15% vai custarR${:.2f}".format(salario, aumento))