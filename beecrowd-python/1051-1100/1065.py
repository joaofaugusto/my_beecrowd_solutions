contador = 0
for _ in range(5):
    n = float(input())
    contador += n % 2 == 0

print(f'{contador} valores pares')
