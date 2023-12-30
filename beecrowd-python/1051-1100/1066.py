contador_par = 0
contador_impar = 0
contador_pos = 0
contador_neg = 0
for _ in range(5):
    n = float(input())
    contador_par += n % 2 == 0 #fez a contagem direto com a operação, foda!!
    contador_impar += n % 2 != 0
    contador_pos += n > 0
    contador_neg += n < 0

print(f'{contador_par} valor(es) par(es)')
print(f'{contador_impar} valor(es) impar(es)')
print(f'{contador_pos} valor(es) positivo(s)')
print(f'{contador_neg} valor(es) negativo(s)')