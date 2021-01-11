def n_primos(n):
    valorInicial = n
    divisor = 2
    while n % divisor != 0 and divisor <= n/2:
        divisor = divisor + 1
    if n % divisor == 0:
        return False
    else:
        return True

n = int(input('Digite um número inteiro: '))

while n > 0:
    if n_primos(n):
        print (n, 'é primo!')
    else:
        print (n, 'não é primo')
    n = int(input('Digite um número inteiro: '))

