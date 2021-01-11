def holerite():
    valorHora = float(input('Entre com o valor da hora: '))
    horasTrabalhadas = float(input('Entre com a quantidade de hoas trabalhadas:'))
    salarioBruto = valorHora * horasTrabalhadas
    porcentagem = calculo_porcentagem(salarioBruto)
    impostoRenda = salarioBruto / 100 * porcentagem
    INSS = salarioBruto / 100 * 10
    FGTS = salarioBruto / 100 * 11
    descontos = impostoRenda + INSS
    print('Salário bruto:      R$',salarioBruto)
    if impostoRenda !=0:
        print('(-) IR (', porcentagem, '%)       R$',impostoRenda)
    print('(-) INSS (10%)      R$', INSS)
    print('FGTS (11%)          R$', FGTS)
    print('Total de descontos: R$', descontos)
    print('Salario Liquido     R$', salarioBruto - descontos)

def calculo_porcentagem(salarioBruto):
    porcento = 0
    if salarioBruto > 900 and salarioBruto <= 1500:
        porcento = 5
    if salarioBruto >1500 and salarioBruto <=2500:
        porcento = 10
    if salarioBruto >2500:
        porcento = 20
    return porcento
