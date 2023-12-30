n = int(input())
limite = 10000

resultados = [i for i in range(1, limite + 1) if i % n == 2]
for j in resultados:
    print(j)