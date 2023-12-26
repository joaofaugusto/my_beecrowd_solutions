entrada = input()
dados = entrada.split()
codigo = int(dados[0])
quantidade = int(dados[1])

# Verificar o código do item
if codigo == 1:
    valor_conta = 4.00 * quantidade
    valor_conta = format(valor_conta, ".2f")
    print("Total: R$ {}".format(valor_conta))
elif codigo == 2:
    valor_conta = 4.50 * quantidade
    valor_conta = format(valor_conta, ".2f")
    print("Total: R$ {}".format(valor_conta))
elif codigo == 3:
    valor_conta = 5.00 * quantidade
    valor_conta = format(valor_conta, ".2f")
    print("Total: R$ {}".format(valor_conta))
elif codigo == 4:
    valor_conta = 2.00 * quantidade
    valor_conta = format(valor_conta, ".2f")
    print("Total: R$ {}".format(valor_conta))
elif codigo == 5:
    valor_conta = 1.50 * quantidade
    valor_conta = format(valor_conta, ".2f")
    print("Total: R$ {}".format(valor_conta))