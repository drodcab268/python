def fun_iva(fact, iva=21):
    return fact + fact * (iva/100)

print(fun_iva(1000))