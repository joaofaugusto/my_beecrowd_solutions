n = int(input())
contador_in = 0
contador_out = 0
i = 1
while i <= n:
    i += 1
    x = int(input())
    contador_in += x >= 10 and x <= 20 
    contador_out += x < 10 or x > 20

print(f'{contador_in} in')
print(f'{contador_out} out') 