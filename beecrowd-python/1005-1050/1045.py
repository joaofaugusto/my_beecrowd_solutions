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
if a >= (b + c): print("NAO FORMA TRIANGULO")
elif (a * a) == ((b * b) + (c * c)): print("TRIANGULO RETANGULO")
elif (a * a) > ((b * b) + (c * c)): print("TRIANGULO OBTUSANGULO")
elif (a * a) < ((b * b) + (c * c)): print("TRIANGULO ACUTANGULO")


if a == b and a == c: print("TRIANGULO EQUILATERO")
elif a == b and c != a and c != b or a == c and b != a and b != c or b == c and a != b and a != c: print("TRIANGULO ISOSCELES")