num=int(input("Introduzca un número entero positivo: "))

for x in range(1,num+1):
    print(x, end=",")
    if (num % x == 0 and x != num and x != 1):
        print(f"El número {num} no es primo")
    else:
        print(f"El número {num} es primo")
        