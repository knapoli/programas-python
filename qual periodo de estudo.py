def qual_periodo_estudo():
    periodo = input('Em qual turno você estuda? Digite M-matutino ou V-Vespertino ou N- Noturno')
    m = 'm'
    n = 'n'
    v = 'v'
    if periodo == m or periodo == v or periodo == n:
        if periodo == m:
            print('Bom dia')
        if periodo == v:
            print('Boa tarde')
        if periodo == n:
            print('Boa noite')
    else:
        print('Valor inválido')