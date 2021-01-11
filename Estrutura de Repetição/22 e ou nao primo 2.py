def n_primos(n):
    valorInicial = n
    divisor = 2
    while n % divisor != 0 and divisor <= n/2:
        divisor = divisor + 1
    if n % divisor == 0:
        return False
    else:
        return True
def divisiveis_por_quais (quais):
    lista = []
    divisor = 2
    contador = 0
    while contador <= quais:
        resto = quais % divisor
        if resto == 0:
            lista.append(divisor)
        divisor = divisor + 1
        contador = contador + 1
    return lista




n = int(input('Digite um número inteiro: '))

while n > 0:
    if n_primos(n):
        print (n, 'é primo!')
    else:
        print (n, 'não é primo')
        quais = divisiveis_por_quais(n)
        print('Este número é divisivel por:', quais)
    n = int(input('Digite um número inteiro: '))


