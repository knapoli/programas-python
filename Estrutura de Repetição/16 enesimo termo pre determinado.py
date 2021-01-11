ultimo = 1
penultimo = 1
print(ultimo,',')
print(penultimo,',')
soma = 1
while soma < 500:
    soma = ultimo + penultimo
    print(soma,',')
    penultimo = ultimo
    ultimo = soma