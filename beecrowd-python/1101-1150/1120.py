d, n = input().split()
if(d == '0' and n == '0'):
    pass
n = '0' + n
val = int(n.replace(d,''))
print(val)