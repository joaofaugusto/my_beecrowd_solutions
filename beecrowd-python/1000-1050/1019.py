entrada = int(input())
horas = entrada // 3600
minutos = (entrada % 3600) // 60
segundos = entrada % 60

print(f"{horas:02d}:{minutos:02d}:{segundos:02d}")
