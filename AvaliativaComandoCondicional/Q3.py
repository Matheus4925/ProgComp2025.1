from random import randint

inicio = 1 # VAI AJUDAR A FAZER A ATUALIZAÇÃO DO INTERVALO 
fim = 100  # VAI AJUDAR A FAZER A ATUALIZAÇÃO DO INTERVALO 

n_sorteado = randint(inicio, fim)  # SORTEIA O NÚMERO ENTRE 1 E 100


print("VOCÊ TEM 4 TENTATIVAS PARA ACERTAR O NÚMERO SORTEADO ENTRE 1 E 100")

# PRIMEIRA TENTATIVA
t1 = int(input( " DIGITE UM NÚMERO ENTRE 1 E 100:  " ))
if t1 == n_sorteado: # VERIFICA SE O NÚMERO DIGITADO É O SORTEADO
    print( " PARABÉNS, VOCÊ ACERTOU O NÚMERO SORTEADO!")
if t1 < n_sorteado: # AQUI DIZ SE O NUMERO DIGITADO É MENOR QUE O SORTEADO
    print("O NÚMERO ESTÁ ENTRE", t1 + 1, "E", fim)
    inicio = t1 + 1  # AQUI ATUALIZA O INTERVALO
elif t1 > n_sorteado: # AQUI DIZ SE O NUMERO DIGITADO É MAIOR QUE O SORTEADO
    print("O NÚMERO ESTÁ ENTRE", inicio, "E", t1 - 1)
    fim = t1 - 1   # AQUI ATUALIZA O INTERVALO

# SEGUNDA TENTATIVA    
t2 = int(input( " SUA SEGUNDA CHANCE DIGITE UM NÚMERO:  " ))
if t2 == n_sorteado:
    print( " PARABÉNS, VOCÊ ACERTOU O NÚMERO SORTEADO!")
if t2 < n_sorteado:
    print("O NÚMERO ESTÁ ENTRE", t2 + 1, "E", fim)
    inicio = t2 + 1
elif t2 > n_sorteado:
    print("O NÚMERO ESTÁ ENTRE", inicio, "E", t2 - 1)
    fim = t2 - 1

# TERCEIRA TENTATIVA
t3 = int(input( " SUA TERCEIRA CHANCE DIGITE UM NÚMERO:  " ))
if t3 == n_sorteado:
    print( " PARABÉNS, VOCÊ ACERTOU O NÚMERO SORTEADO!")
if t3 < n_sorteado:
    print("O NÚMERO ESTÁ ENTRE", t3 + 1, "E", fim)  
    inicio = t3 + 1
elif t3 > n_sorteado:
    print("O NÚMERO ESTÁ ENTRE", inicio, "E", t3 - 1)
    fim = t3 - 1

# ULTIMA TENTATIVA
t4 = int(input( " SUA QUARTA E ÚLTIMA CHANCE, DIGITE UM NÚMERO:  " ))
if t4 == n_sorteado:
    print( " PARABÉNS, VOCÊ ACERTOU O NÚMERO SORTEADO!")
else:
    print ( " VOCÊ PERDEU, O NÚMERO SORTEADO FOI", n_sorteado)
    
