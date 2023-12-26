entrada = float(input())
inicio1 = 0
limite1 = 25.000000000000
inicio2 = 25.000000000001
limite2 = 50.00000000000
inicio3 = 50.000000000001
limite3 = 75.000000000000
inicio4 = 75.0000000000001
limite4 = 100.0000000000000

if entrada >= inicio1 and entrada <= limite1:
    print("Intervalo [0,25]")
elif entrada >= inicio2 and entrada <= limite2:
    print("Intervalo (25,50]")
elif entrada >= inicio3 and entrada <= limite3:
    print("Intervalo (50,75]")
elif entrada >= inicio4 and entrada <= limite4:
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")