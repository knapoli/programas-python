import emoji
print(emoji.emojize('Python is :thumbs_up:'))

dias = int(input("Quantos dias alugados? "))
km = float(input("Quantos Km rodados? "))
total = (dias * 60) + (km * 0.15)
print("O total a pagar é de R${:.2f}".format(total))