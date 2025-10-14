num1=int(input("Introduzca el dividendo: "))
num2=int(input("Introduzca el divisor: "))


div=(num1/num2)

if (num1%num2) == (0):
    print("Error!")
else:
    print(f"({num1} / {num2}) = {div}")


