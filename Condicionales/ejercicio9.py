edad=int(input("Introduzac su edad: "))

if edad < 4:
    print("Entrada: 0€")
elif edad >= 4 and edad < 18:
    print("Entrada: 5€")
else:
    print("Entrada: 10€")