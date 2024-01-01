while True:
    a, b = map(int, input().split())
    if a <= 0 or b <= 0:
        break

    minimo = min(a, b)
    maximo = max(a, b)
    soma = sum(range(minimo, maximo + 1))

    print(' '.join(map(str, range(minimo, maximo + 1))), end=" ")
    print('Sum=%d' % soma)
