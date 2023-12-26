entrada1 = input()
dados1 = entrada1.split()
npecas1 = int(dados1[1])
valorpeca1 = float(dados1[2])

entrada2 = input()
dados2 = entrada2.split()
npecas2 = int(dados2[1])
valorpeca2 = float(dados2[2])


valortotal = (npecas1 * valorpeca1) + (npecas2 * valorpeca2)
print("VALOR A PAGAR: R$ %.2f" % valortotal)