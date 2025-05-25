print("DIGITE UMA DATA INICIAL E UMA DATA FINAL PARA SABER O NÚMERO DE DIAS DECORRIDOS ENTRE ELAS.")
print("DIGITE A DATA INICIAL.")
dia_inicio = int(input("DIA: "))
mes_inicio = int(input("MÊS: "))

# VERIFICANDO SE A DATA INICIAL É VÁLIDA.
if mes_inicio < 1 or mes_inicio > 12:
    print("MÊS INICIAL INVÁLIDO!")
else:
    if mes_inicio == 1 or mes_inicio == 3 or mes_inicio == 5 or mes_inicio == 7 or mes_inicio == 8 or mes_inicio == 10 or mes_inicio == 12: # MESES COM 31 DIAS.
        max_dia_inicio = 31 # PARA VEIFICAR MAXIMO DE DIAS.
    elif mes_inicio == 4 or mes_inicio == 6 or mes_inicio == 9 or mes_inicio == 11: # MESES COM 30 DIAS.
        max_dia_inicio = 30
    elif mes_inicio == 2: # FEVEREIRO ELE NÃO É BISEXTO.
        max_dia_inicio = 28
    else:
        max_dia_inicio = 0  # PARA DIA 0 SER INVÁLIDO.

    if dia_inicio < 1 or dia_inicio > max_dia_inicio: # VERIFICANDO SE O DIA É VÁLIDO.
        print(" ESSE DIA NÃO EXISTE NO MÊS!")
    else:
        # DIGITE A DATA FINAL
        print("DIGITE A DATA FINAL.")
        dia_fim = int(input("DIA: "))
        mes_fim = int(input("MÊS: "))

        if mes_fim < 1 or mes_fim > 12:
            print(" ESSE MÊS NÃO EXISTE!")
        else: #MESMA COICA DA DATA INICIAL SO QUE AQUI ESTA FERIFICANDO A DATA FINAL.
            if mes_fim == 1 or mes_fim == 3 or mes_fim == 5 or mes_fim == 7 or mes_fim == 8 or mes_fim == 10 or mes_fim == 12: 
                max_dia_fim = 31
            elif mes_fim == 4 or mes_fim == 6 or mes_fim == 9 or mes_fim == 11:
                max_dia_fim = 30
            elif mes_fim == 2:
                max_dia_fim = 28
            else:
                max_dia_fim = 0

            if dia_fim < 1 or dia_fim > max_dia_fim:
                print("ESSE DIA NÃO EXISTE NO MÊS!")
            else:
                # CCONVERTER DATA INICIAL EM DIA DO ANO.
                dias_ano_inicio = 0
                if mes_inicio > 1:
                    dias_ano_inicio += 31
                if mes_inicio > 2:
                    dias_ano_inicio += 28
                if mes_inicio > 3:
                    dias_ano_inicio += 31
                if mes_inicio > 4:
                    dias_ano_inicio += 30
                if mes_inicio > 5:
                    dias_ano_inicio += 31
                if mes_inicio > 6:
                    dias_ano_inicio += 30
                if mes_inicio > 7:
                    dias_ano_inicio += 31
                if mes_inicio > 8:
                    dias_ano_inicio += 31
                if mes_inicio > 9:
                    dias_ano_inicio += 30
                if mes_inicio > 10:
                    dias_ano_inicio += 31
                if mes_inicio > 11:
                    dias_ano_inicio += 30
                dias_ano_inicio += dia_inicio

                # CONVERTER DATA FINAL EM DIA DO ANO.
                dias_ano_fim = 0
                if mes_fim > 1:
                    dias_ano_fim += 31
                if mes_fim > 2:
                    dias_ano_fim += 28
                if mes_fim > 3:
                    dias_ano_fim += 31
                if mes_fim > 4:
                    dias_ano_fim += 30
                if mes_fim > 5:
                    dias_ano_fim += 31
                if mes_fim > 6:
                    dias_ano_fim += 30
                if mes_fim > 7:
                    dias_ano_fim += 31
                if mes_fim > 8:
                    dias_ano_fim += 31
                if mes_fim > 9:
                    dias_ano_fim += 30
                if mes_fim > 10:
                    dias_ano_fim += 31
                if mes_fim > 11:
                    dias_ano_fim += 30
                dias_ano_fim += dia_fim

                # VERIFICANDO SE A DATA FINAL É MAIOR QUE A DATA INICIAL.
                if dias_ano_fim < dias_ano_inicio: 
                    print(" A DATA FINAL É MENOR QUE A DATA INICIAL!")
                else:
                    dias_decorridos = dias_ano_fim - dias_ano_inicio
                    print(" ENTRE DIA INICIAL E DIA FINAL SE PASSARAM: ", dias_decorridos, " DIAS.")


  
