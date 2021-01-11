repetir = 1
while repetir == 1:
    paisA = float(input('Entre com a população do pais A: '))
    taxaA = float(input('Entre com a taxa do pais A: '))
    paisB = float(input('Entre com a população do pais B: '))
    taxaB = float(input('Entre com a taxa do pais B: '))
    ano = 0
    if paisA < paisB:
        while paisA <= paisB:
            paisA = paisA + (paisA / 100 * taxaA)
            paisB = paisB + (paisB / 100 * taxaB)
            ano = ano + 1
    if paisA > paisA:
        while paisB <= paisA:
            paisA = paisA + (paisA / 100 * taxaA)
            paisB = paisB + (paisB / 100 * taxaB)
            ano = ano + 1

    print('paisA', paisA)
    print('paisB', paisB)
    print('ano', ano)
    repetir = int(input('Entre com 1 para continuar: '))