entrada = input()
dados = entrada.split()
a = int(dados[0])
b = int(dados[1])
c = int(dados[2])
d = int(dados[3])

if b > c and d > a and (c + d) > (a + b) and c >= 1 and d >=1 and (a % 2) == 0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")