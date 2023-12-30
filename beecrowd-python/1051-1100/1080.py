maior = 0
loc = 0
for i in range(3):
    n = int(input())
    if n > maior:
        maior = n
        loc = i + 1


print(f'{maior}')
print(f'{loc}')
