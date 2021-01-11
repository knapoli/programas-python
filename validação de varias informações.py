nome = input('Entre com o mome ')
while len(nome) <= 3:
    nome = input('Nome precisa ser ter mais que 3 caracteres ')
idade = int(input('Entre com a idade '))
while idade <0 or idade >150:
    idade = int(input('Idade inválida, entre com a idade '))
salario = float(input('Entre com o salario '))
while salario < 0:
    salario = float(input('Salário precisa ser maior que zero. Entre com o salario '))
sexo = input('Entre com m para masculino e f para feminino ')
while sexo != 'f' and sexo != 'm':
    sexo = input('Entre com m para masculino e f para feminino ')
estadoc = input('Estado Civil: s, c, v, d')
while estadoc != 's' and estadoc != 'c' and estadoc != 'v' and estadoc != 'd':
    estadoc = input('Nao tem estado civil confuso ')

