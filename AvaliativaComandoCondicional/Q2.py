print("CALCULANDO A MÉDIA")
nota1 = float(input( " DIGITE A SUA PRIMEIRA NOTA:  "))
nota2 = float(input( " DIGITE A SUA SEGUNDA NOTA:  "))

media = (( nota1 * 2 ) + ( nota2 * 3)) / 5 # CALCULANDO A MÉDIA FINAL.

if media >= 6.0:
    print("APROVADO, SUA MÉDIA FICOU EM ", media) # SE APROVADO ACABA AQUI.

else: 
    print("PROVA FINAL, SUA MÉDIA FICOU EM " , media) # SE REPROVADO, VAI PARA A PROVA FINAL.
    
    notaf = float (input( " DIGITE A SUA NOTA FINAL:  "))  # PEDINDO A NOTA DA PROVA FINAL >

    media = (( nota1 * 2) + ( notaf * 3 )) / 5 # CALCULANDO UMA DAS NOTAS COM A PROVA FINAL.

    if media >= 6.0:
        print("APROVADO, SUA MÉDIA FICOU EM ", media) 
    else:
        print("REPROVADO, SUA MÉDIA FICOU EM ", media)
