a, b, c, d = map(int, input().split())
if a == c and b == d:
    aux = 24
    aux2 = 0
    print("O JOGO DUROU %s HORA(S) E %s MINUTO(S)" % (aux, aux2))

if c > a and d > b:
    aux = c - a
    aux2 = d - b
    print("O JOGO DUROU %s HORA(S) E %s MINUTO(S)" % (aux, aux2))
    
if c > a and d < b:
    aux = (c - a) - 1
    aux2 = 60 - (b - d)
    print("O JOGO DUROU %s HORA(S) E %s MINUTO(S)" % (aux, aux2))

if c == a and d < b:
    aux = 23
    aux2 = 60 - (b - d)
    print("O JOGO DUROU %s HORA(S) E %s MINUTO(S)" % (aux, aux2))

if c == a and d > b:
    aux = 0
    aux2 = d - b
    print("O JOGO DUROU %s HORA(S) E %s MINUTO(S)" % (aux, aux2))
    
if c > a and d == b:
    aux = c - a
    aux2 = 0
    print("O JOGO DUROU %s HORA(S) E %s MINUTO(S)" % (aux, aux2))

if c < a and d < b:
    aux = 23 - (a - c)
    aux2 = 60 - (b - d)
    print("O JOGO DUROU %s HORA(S) E %s MINUTO(S)" % (aux, aux2))

if c < a and d > b:
    aux = 24 - (a - c)
    aux2 = d - b
    print("O JOGO DUROU %s HORA(S) E %s MINUTO(S)" % (aux, aux2))
    
if c < a and d == b:
    aux = 24 - (a - c)
    aux2 = 0
    print("O JOGO DUROU %s HORA(S) E %s MINUTO(S)" % (aux, aux2))