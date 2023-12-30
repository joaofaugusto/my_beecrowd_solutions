x, y, = int(input()), int(input())
maior = max(x, y)
menor = min(x, y)+1
if (menor % 2) == 0:
    menor += 1
soma = 0
for i in range(menor, maior, 2):
    soma += i
print(soma)
