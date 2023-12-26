entrada = int(input())
minutos = entrada // 60
horas = minutos // 60
segundos = entrada - (60 * minutos)
if minutos > 60:
    minutos2 = minutos % 60
    print ("%d:%d:%d" % (horas, minutos2, segundos))
else:
    print("%d:%d:%d" % (horas, minutos, segundos)) 