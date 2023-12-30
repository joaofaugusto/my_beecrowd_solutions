n = int(input())
limite = n + 1
for i in range(1, limite):
    if (i % 2) == 0:
        q = i ** 2
        print(f'{i}^2 = {q}')