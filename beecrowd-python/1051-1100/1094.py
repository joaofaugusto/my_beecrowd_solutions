n = int(input())
soma_r = 0
soma_s = 0
soma_c = 0
for i in range(n):
    x = input().split()
    if x[1] == "R":
        soma_r += int(x[0])  
    if x[1] == "S":
        soma_s += int(x[0])
    if x[1] == "C":
        soma_c += int(x[0])  
soma_total = soma_r + soma_c
soma_total = soma_total + soma_s
p_r = soma_r / soma_total
p_r = p_r * 100
p_s = soma_s / soma_total
p_s = p_s * 100
p_c = soma_c / soma_total
p_c = p_c * 100

print(f'Total: {soma_total} cobaias')
print(f'Total de coelhos: {soma_c}')
print(f'Total de ratos: {soma_r}')
print(f'Total de sapos: {soma_s}')
print(f'Percentual de coelhos: {p_c:.2f} %')
print(f'Percentual de ratos: {p_r:.2f} %')
print(f'Percentual de sapos: {p_s:.2f} %')

