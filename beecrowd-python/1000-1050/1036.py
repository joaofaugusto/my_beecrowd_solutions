entrada = input()
dados = entrada.split()

a = float(dados[0])
b = float(dados[1])
c = float(dados[2])

if a == 0:
    print("Impossivel calcular")
else:
    delta = (b ** 2) - 4 * a * c
    if delta == 0 or delta < 0:
        print("Impossivel calcular")
    else:
        r1 = ((-b) + (delta ** 0.5)) / (2 * a)
        r2 = ((-b) - (delta ** 0.5)) / (2 * a)
        print("R1 = %.5f" % r1)
        print("R2 = %.5f" % r2)