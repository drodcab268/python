def fun_factorial(num):
    fact = 1
    for i in range(num):
        fact *= i+1
    return fact

print(fun_factorial(22))