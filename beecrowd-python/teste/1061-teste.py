dia, dia_i = input().split()
dia_i = int(dia_i)
hora_i, minuto_i, segundo_i = map(int, input().split(":"))

dia, dia_f = input().split()
dia_f = int(dia_f)
hora_f, minuto_f, segundo_f = map(int, input().split(":"))

a = minuto_i * 60
b = a + segundo_i
c = hora_i * 3600
d = dia_i * 86400
n1 = b + c + d

e = minuto_f * 60
f = e + segundo_f
g = hora_f * 3600
h = dia_f * 86400
n2 = f + g + h

diferenca_segundos = n2 - n1

dias = diferenca_segundos // 86400
x = diferenca_segundos % 86400
horas = x // 3600

y = diferenca_segundos % 3600
minutos = y // 60
segundos = diferenca_segundos % 60

print(f'{dias} dia(s)')
print(f'{horas} hora(s)')
print(f'{minutos} minuto(s)')
print(f'{segundos} segundo(s)')
