entrada = int(input())
brasilia = 61
salvador = 71
sao_paulo = 11
rio_de_janeiro = 21
juiz_de_fora = 32
campinas = 19
vitoria = 27
belo_horizonte = 31

lista = [61,71,11,21,32,19,27,31]

if entrada == brasilia: print("Brasilia")
if entrada == salvador: print("Salvador")
if entrada == sao_paulo: print("Sao Paulo")
if entrada == rio_de_janeiro: print("Rio de Janeiro")
if entrada == juiz_de_fora: print("Juiz de Fora")
if entrada == campinas: print("Campinas")
if entrada == vitoria: print("Vitoria")
if entrada == belo_horizonte: print("Belo Horizonte")

if entrada not in lista:
    print("DDD nao cadastrado")