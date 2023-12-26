entrada = float(input())
if entrada < 2000.00: print("Isento")
else:
    if entrada > 2000 and entrada <= 3000:
        aux = entrada - 2000
        resultado = aux * 0.08
        print("R$ %.2f" % resultado)
    elif entrada > 3000 and entrada < 4500:
        aux = entrada - 3000
        resultado = (aux * 0.18) + (1000 * 0.08)
        print("R$ %.2f" % resultado)    
    else:
        aux = entrada - 4500
        resultado = (aux * 0.28) + (1000 * 0.08) + (1500 * 0.18)
        print("R$ %.2f" % resultado)    
        
        