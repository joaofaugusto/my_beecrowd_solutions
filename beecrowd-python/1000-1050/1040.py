entrada = input()
dados = entrada.split()
nota1 = float(dados[0])
nota2 = float(dados[1])
nota3 = float(dados[2])
nota4 = float(dados[3])

soma_com_fatores = (nota1 * 2) + (nota2 * 3) + (nota3 * 4) + (nota4 * 1) 
media = float(soma_com_fatores) / 10
if media >= 7.0:
    print("Media: %.1f" % media)
    print("Aluno aprovado.")
if media < 5.0:
    print("Media: %.1f" % media)
    print("Aluno reprovado.")
if media >= 5 and media <= 6.9:
    print("Media: %.1f" % media)
    print("Aluno em exame.")
    exame = float(input())
    print("Nota do exame: %.1f" % exame)
    resultado = (media + exame) / 2
    if resultado >= 5.0:
        print("Aluno aprovado.")
        print("Media final: %.1f" % resultado)
    if resultado <= 4.9:
        print("Aluno reprovado.")
        print("Media final: %.1f" % resultado)
