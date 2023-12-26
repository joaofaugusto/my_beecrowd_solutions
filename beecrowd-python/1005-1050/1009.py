nome = input()
salario_fixo = float(input())
vendas = float(input())
fator_bonus = 0.15
valor_com_bonus = (vendas * fator_bonus) + salario_fixo
print("TOTAL = R$ %.2f" % valor_com_bonus)