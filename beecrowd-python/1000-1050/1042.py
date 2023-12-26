entrada = input()
dados = entrada.split()
lista_ordenada = [int(dados[0]), int(dados[1]), int(dados[2])]
lista_normal = [dados[0], dados[1], dados[2]]

lista_ordenada.sort()
print(lista_ordenada[0])
print(lista_ordenada[1])
print(lista_ordenada[2])

print("")

print(lista_normal[0])
print(lista_normal[1])
print(lista_normal[2])

