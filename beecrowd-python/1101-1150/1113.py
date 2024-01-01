while True:
    try:
        a, b = map(int, input().split())
        if a == b: break
        elif a > b: print("Decrescente")
        else: print("Crescente")
    except EOFError:
        break