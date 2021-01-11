numero = int(input("Digite um número para ver sua tabuada: "))
contador = 1
while contador <= 20:
    multiplicacao = numero * contador
    print (numero, "X", contador, "=", multiplicacao)
    contador = contador + 1