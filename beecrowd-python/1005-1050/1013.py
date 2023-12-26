entrada = input()
dados = entrada.split()

x = int(dados[0])
y = int(dados[1])
z = int(dados[2])

if x >= y and x >= z: print(str(x) + " eh o maior")
if y > x and y >= z: print(str(y) + " eh o maior")
if z > x and z > y: print(str(z) + " eh o maior")
