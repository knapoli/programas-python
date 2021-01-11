ultimo = 1
penultimo = 1
enesimoTermo = int(input('Entre com o n−ésimo termo: '))
contaElementos = 3
print(ultimo,',')
print(penultimo,',')
while contaElementos <= enesimoTermo:
    soma = ultimo + penultimo
    print(soma,',')
    penultimo = ultimo
    ultimo = soma
    contaElementos = contaElementos + 1