def fun_mcd(num1, num2):
    resto = 0
    while(num2 > 0):
        resto = num2
        num2 = num1 % num2
        num1 = resto
    return num1

def fun_mcm(num1, num2):
    if num1 > num2:
        mayor = num1
    else:
        mayor = num2
    while (mayor % num1 != 0) or (mayor % num2 != 0):
        mayor += 1
    return mayor

print(fun_mcd(77,66))