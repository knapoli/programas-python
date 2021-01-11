nome = input('Entre com o nome: ')
while len(nome) <= 3:
    nome = input('Entre com o nome maior que 3 caracteres: ')

idade = int(input('Entre com a idade: '))
while idade < 0 or idade > 150:
    idade = int(input('Idade deve estar entre 0 e 150: '))

salario = float(input('Entre com o salario: '))
while salario <= 0:
    salario = float(input('Salario deve ser maior que 0: '))

sexo = str(input('Entre com (f) para feminino ou (m) para masculino: '))
validos = ['f', 'm']
verificador = False
while verificador == False:
    if sexo in validos:
        verificador = True
    else:
        sexo = str(input('Entre com (f) para feminino ou (m) para masculino: '))

estadoCivil = str(input('Entre com (s) para solteiro or (c) para casado ou (v) para viuvo, ou (d) para disquitado: '))
ListaDosValidos = ['s', 'c', 'v', 'd']
verificador = False
while verificador == False:
    if estadoCivil in ListaDosValidos:
        verificador = True
    else:
        sexo = str(input('Entre com (s) para solteiro or (c) para casado ou (v) para viuvo, ou (d) para disquitado: '))