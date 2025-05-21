n = int(input("Informe um número de 4 algarismos:"))
soma = 0

if 999 > n or n > 9999:
    print("Esse número não possui 4 algarismos.")
    
else:
    n != 0
    r = n % 10
    n = n // 10
    soma = soma + r
    if n != 0:
        r = n % 10
        n = n // 10
        soma = soma + r
    if n != 0:
        r = n % 10
        n = n // 10
        soma = soma + r
    if n != 0:
        r = n % 10
        n = n // 10
        soma = soma + r
        print("Soma:", soma)