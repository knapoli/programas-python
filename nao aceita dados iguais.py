nome = input('Entre com o mome ')
idade = int(input('Entre com a idade '))
salario = float(input('Entre com o salario '))
sexo = input('Entre com m para masculino e f para feminino ')
estadoc = input('Estado Civil: s, c, v, d')

while len(nome) <= 3:
    nome = input('Nome precisa ser ter mais que 3 caracteres ')