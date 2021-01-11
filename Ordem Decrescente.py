def pega_numeros():
    num1 = int(input('Qual o primeiro número? '))
    num2 = int(input('Qual é o segundo número? '))
    num3 = int(input('Qual é o terceiro número? '))
    lista = [num1, num2, num3]
    return lista

def ordem_decrescente():
    valores = pega_numeros()
    nova = sorted(valores, reverse=True)
    print(nova)