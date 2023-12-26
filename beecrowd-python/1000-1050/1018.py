entrada = int(input())
print(entrada)

cem = entrada // 100
print("%s nota(s) de R$ 100,00" % cem)
aux = entrada % 100

cinquen = aux // 50
print("%s nota(s) de R$ 50,00" % cinquen)
aux = aux % 50

vinte = aux // 20
print("%s nota(s) de R$ 20,00" % vinte)
aux = aux % 20

dez = aux // 10
print("%s nota(s) de R$ 10,00" % dez)
aux = aux % 10

cinco = aux // 5
print("%s nota(s) de R$ 5,00" % cinco)
aux = aux % 5

dois = aux // 2
print("%s nota(s) de R$ 2,00" % dois)
aux = aux % 2

um = aux // 1
print("%s nota(s) de R$ 1,00" % um)


