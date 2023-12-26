a, b, c = map(float, input().split())
if(a < b):
    temp = a
    a = b
    b = temp
if(b < c):
    temp = b
    b = c
    c = temp
if(a < b):
    temp = a
    a = b
    b = temp

n = (a * a)
x = (b * b)
y = c * c
z = (x + y)
w = b + c
if a >= w: print("NAO FORMA TRIANGULO")
elif n == z: print("TRIANGULO RETANGULO")
elif n > z: print("TRIANGULO OBTUSANGULO")
elif n < z: print("TRIANGULO ACUTANGULO")


if a == b and a == c: print("TRIANGULO EQUILATERO")
elif a == b and c != a and c != b or a == c and b != a and b != c or b == c and a != b and a != c: print("TRIANGULO ISOSCELES")