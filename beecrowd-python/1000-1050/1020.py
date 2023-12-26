entrada = int(input())
anos = (entrada // 30) // 12
meses = (entrada - (anos * 365)) // 30
dias = entrada - (anos * 365 + meses * 30) 
if meses >= 12:
    meses2 = meses // 12
    print("%d ano(s)" % anos)
    print("%d mes(es)" % meses2)
    print("%d dia(s)" % dias)
else:
    print("%d ano(s)" % anos)
    print("%d mes(es)" % meses)
    print("%d dia(s)" % dias)
