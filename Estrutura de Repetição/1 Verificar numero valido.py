nota = int(input('Entre com uma nota: '))
validos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
repetidor = False
while repetidor == False:
    if nota in validos:
        repetidor = True
    else:
        nota = int(input('Número inválido, Entre com uma nota válida: '))
print('Obrigado pela sua avaliação.')