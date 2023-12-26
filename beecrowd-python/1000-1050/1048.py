a = float(input())
reajuste1 = 1.15
reajuste2 = 1.12
reajuste3 = 1.10
reajuste4 = 1.07
reajuste5 = 1.04
if a >= 0 and a <= 400.00:
    resultado = a * reajuste1
    print("Novo salario: %.2f" % resultado)
    print("Reajuste ganho: %.2f" % (resultado - a))
    print("Em percentual: 15 %")
elif a >= 400.01 and a <= 800.0: 
    resultado = a * reajuste2
    print("Novo salario: %.2f" % resultado)
    print("Reajuste ganho: %.2f" % (resultado - a))
    print("Em percentual: 12 %")
elif a >= 800.01 and a <= 1200.00:
    resultado = a * reajuste3
    print("Novo salario: %.2f" % resultado)
    print("Reajuste ganho: %.2f" % (resultado - a))
    print("Em percentual: 10 %")
elif a >= 1200.01 and a <= 2000.00:
    resultado = a * reajuste4
    print("Novo salario: %.2f" % resultado)
    print("Reajuste ganho: %.2f" % (resultado - a))
    print("Em percentual: 7 %")
elif a >= 2000.01:
    resultado = a * reajuste5
    print("Novo salario: %.2f" % resultado)
    print("Reajuste ganho: %.2f" % (resultado - a))
    print("Em percentual: 4 %")