a1 = float(input())
a2 = float(input())
a3 = float(input())
a4 = float(input())
a5 = float(input())
a6 = float(input())
lista = []
if a1 > 0:
    lista.append(a1)
if a2 > 0:
    lista.append(a2)
if a3 > 0:
    lista.append(a3)
if a4 > 0:
    lista.append(a4)
if a5 > 0:
    lista.append(a5)
if a6 > 0:
    lista.append(a6)

qtd = len(lista)
print("%d valores positivos" % qtd)