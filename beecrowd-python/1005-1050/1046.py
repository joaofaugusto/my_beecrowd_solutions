a, b = map(int, input().split())
meianoite = 24
if b < a:
    aux = meianoite - a
    aux += b
    print("O JOGO DUROU %d HORA(S)" % aux)
elif b > a:
    aux = b - a
    print("O JOGO DUROU %d HORA(S)" % aux)
elif a == 0 and b == 0:
    aux = 24
    print("O JOGO DUROU %d HORA(S)" % aux)
elif a == b:
    aux = 24
    print("O JOGO DUROU %d HORA(S)" % aux)
    