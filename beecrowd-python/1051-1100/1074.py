n = int(input())
for i in range(n):
    x = int(input())
    if x == 0:
        print(f'NULL')
    if (x % 2) == 0 and x > 0:
        print(f'EVEN POSITIVE')
    if (x % 2) == 0 and x < 0 :
        print(f'EVEN NEGATIVE')
    if (x % 2) != 0 and x > 0:
        print(f'ODD POSITIVE')
    if (x % 2) != 0 and x < 0:
        print(f'ODD NEGATIVE')
    