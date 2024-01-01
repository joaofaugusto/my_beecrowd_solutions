contador = 0
for _ in range(5):
    n = float(input())
    contador += n % 2 == 0 #fez a contagem direto com a operação, foda!!

print(f'{contador} valores pares')
