nota1 = int(input("Insira a sua nota no 1º bimestre:"))
nota2 = int(input("Insira a sua nota no 2º bimestre:"))

md = (2 * nota1 + 3 * nota2)// 5
if 20 <= md < 60:
    print("Você realizou a prova final.")
    notaf = int(input("Insira sua nota na prova final:"))
    mdf = (md + notaf)// 2
    if mdf < 60:
        print("Você foi reprovado")
    else:
        print("Você foi aprovado.")
else:
    if 20 > md:
        print("Você foi reprovado")
    if md >= 60:
        print("Você foi aprovado.")

