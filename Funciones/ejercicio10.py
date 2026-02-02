def fun_decimal(num):
    num = list(num)
    num.reverse()
    decimal = 0
    for i in range(len(num)):
        decimal += int(num[i]) * 2 ** i
    return decimal

def fun_binario(num):
    binario = []
    while num > 0:
        binario.append(str(num % 2))
        num //= 2
    binario.reverse()
    return "".join(binario)

print(fun_decimal("11110000"))
print(fun_binario(77))