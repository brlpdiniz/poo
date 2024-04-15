# FASE 1 --------------------------------------
def calcular_imposto(valor):
    ir = valor * 0.275
    iss = valor * 0.05
    csll = valor * 0.0375
    pis = valor * 0.03
    return ir + iss + csll + pis

print(calcular_imposto(1000))


# FASE 2 --------------------------------------
def calcular_imposto2(valor, perc_ir):
    ir = valor * perc_ir
    iss = valor * 0.05
    csll = valor * 0.0375
    pis = valor * 0.03
    return ir + iss + csll + pis

print(calcular_imposto2(perc_ir=0.0275, valor=1000))


# ARGS --------------------------------------
def calcular_imposto3(valor, *args):
    total_imposto = 0
    print(args)
    return total_imposto

print(calcular_imposto3(1000, 0.25, 0.15, 15, 10))


# ARGS --------------------------------------
def calcular_imposto4(valor, *args):
    total_imposto = 0
    for item in args:
        total_imposto += valor * item
    return total_imposto

print(calcular_imposto4(1000, 0.275, 0.05, 0.0375, 0.03))


# KWARGS --------------------------------------
def calcular_impost5(valor, **kwargs):
    total_imposto = 0
    print(kwargs)
    return total_imposto

print(calcular_impost5(1000, perc_ir = 0.275, perc_iss = 0.05, perc_csll = 0.0375, perc_is = 0.03))