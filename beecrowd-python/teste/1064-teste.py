contador = 0
soma = 0
for i in range(1, 7):
    n = float(input())
    if n > 0:
        soma = soma + n
        contador += 1

media = soma / contador
print(f'{contador} valores positivos')
print(f'{media:.1f}')