largura = int(input('Digite a largura: '))
altura = int(input('Digite a altura: '))
guardar = largura
guardarAltura = altura

while altura > 0:
    largura = guardar
    if altura == guardarAltura or altura == 1:
        while largura >0:
            print('#', end = '')
            largura = largura - 1
    else:
        while largura >0:
            if largura == guardar or largura == 1:
                print('#', end = '')
                largura = largura - 1
            else:
                print(' ', end = '')
                largura = largura - 1
    altura = altura - 1
    print ()
