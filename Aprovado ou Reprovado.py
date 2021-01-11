def confere_aprovacao():
    nota1 = float(input('Entre com a primeira nota: '))
    nota2 = float(input('Entre com a segunda nota: '))
    media = (nota1 + nota2) / 2
    conceito = retorna_conceito(media)
    lista1 = ['A', 'B', 'C']
    print('Sua primeira nota foi: ', nota1)
    print('Sua segunda nota foi: ', nota2)
    print('Sua primeira media foi: ', media)
    print('Seu conceito foi: ', conceito)
    if conceito in lista1:
        print('Aprovado')
    else:
        print('Reprovado')

def retorna_conceito (media):
    if media >= 9:
        return 'A'
    if media >= 7.5 and media < 9:
        return 'B'
    if media >= 6 and media < 7.5:
        return 'C'
    if media >= 4 and media < 6:
        return 'D'
    if media >= 0 and media < 4:
        return 'E'

def testa_aprovacao(media, b):
    conceito = retorna_conceito(media)
    if conceito != b:
        print('Errado para media', media)

def testa_conceito():
    testa_aprovacao(10, 'A')
    testa_aprovacao(9, 'A')
    testa_aprovacao(8, 'B')
    testa_aprovacao(7, 'B')
    testa_aprovacao(6, 'C')
    testa_aprovacao(5, 'D')
    testa_aprovacao(4, 'D')
    testa_aprovacao(3, 'E')
    testa_aprovacao(2, 'E')
    testa_aprovacao(1, 'E')
    testa_aprovacao(0, 'E')
    testa_aprovacao(7.5, 'B')


