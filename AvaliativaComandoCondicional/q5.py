tempo = int(input("Informe o tempo estacionado em minutos:"))

# Verificação se há fração de hora
if tempo % 60 == 0:
    tempo = tempo // 60
else:
    tempo = tempo // 60 + 1

# Cálculo do valor total
if tempo <= 1:
    valor = 8
    print(f"Você irá pagar R${valor}.")
elif tempo <= 2:
    valor = 16
    print(f"Você irá pagar R${valor}.")
elif tempo <= 3:
    valor = 21
    print(f"Você irá pagar R${valor}.")
elif tempo <= 4:
    valor = 26
    print(f"Você irá pagar R${valor}.")
elif 4 < tempo < 12:
    valor = 26 + (tempo-4) * 3
    print(f"Você irá pagar R${valor}.")
elif tempo > 12:
    valor = 30
    print(f"Você irá pagar R${valor}.")
