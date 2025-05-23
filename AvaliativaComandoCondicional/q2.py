# Entrada da nota
nota1 = int(input("Digite a sua nota no 1º bimestre:"))
nota2 = int(input("Digite a sua nota no 2º bimestre:"))

# Cálculo para a nota do aluno
média = (2 * nota1 + 3 * nota2)// 5

# Verificação da situação do aluno
if média > 60:
    print("Você foi aprovado.")
elif 20 <= média < 60:
    print("Você realizou a prova final.")
    nota_final = int(input("Digite sua nota na prova final:"))
    média_final = (média + nota_final)// 2
    if média_final < 60:
        print("Você foi reprovado")
    else:
        print("Você foi aprovado.")
else:
    print("Você foi reprovado.")
