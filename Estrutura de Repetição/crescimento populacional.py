paisA = float(80.000)
paisB = float(200.000)
ano = 0
while paisA <= paisB:
    paisA = paisA + (paisA / 100 * 3)
    paisB = paisB + (paisB / 100 * 1.5)
    ano = ano + 1

print('paisA', paisA)
print('paisB', paisB)
print('ano', ano)