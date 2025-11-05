num=int(input("Introduzca un número entero positivo: "))
for i in range(1,num+1,2):
    print()
    for j in range(i,0,-2):
        print(j, end=",")
print()
