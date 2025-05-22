n = int(input("Digite um número de até 4 algarismos:"))
soma = 0

if n < 1 or n > 9999:
    print("Esse número possui mais de 4 algarismos.")
    
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
