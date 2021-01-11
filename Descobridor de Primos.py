def n_primos(n):
    primo = 2
    contador = 0
    while n >= primo:
        divisor = 2
        while primo % divisor != 0 and divisor <= primo/2:
            divisor = divisor + 1
        if primo % divisor != 0 or primo == 2:
            primo = primo + 1
        primo = primo + 1
    print(primo)
