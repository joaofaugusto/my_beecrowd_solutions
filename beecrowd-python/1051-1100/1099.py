n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    maximo = max(x, y)
    minimo = min(x, y)
    teste = []
    a = minimo + 1
    for j in range(a, maximo):
        if j % 2 == 1:
            teste.append(j)
    aux = sum(teste)
    print(aux)