entrada = input()
dados = entrada.split()
n1 = float(dados[0])
n2 = float(dados[1])
n3 = float(dados[2])
pi = 3.14159

area_triangulo = (n1 * n3) / 2
area_circulo = (n3 ** 2) * pi
area_trapezio = ((n1 + n2) * n3) / 2
area_quadrado = n2 ** 2
area_retangulo = n1 * n2

print("TRIANGULO: %.3f" % area_triangulo)
print("CIRCULO: %.3f" % area_circulo)
print("TRAPEZIO: %.3f" % area_trapezio)
print("QUADRADO: %.3f" % area_quadrado)
print("RETANGULO: %.3f" % area_retangulo)
