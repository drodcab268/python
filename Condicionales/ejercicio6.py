nombre=input("Introduzca su nombre: ")
sexo=input("Introduzca su sexo (F o M): ")

if sexo == "F":
    if nombre[0]== "A" or nombre[0]== "B" or nombre[0]== "C" or nombre[0]== "D" or nombre[0]== "E" or nombre[0]== "F" or nombre[0]== "G" or nombre[0]== "H" or nombre[0]== "I" or nombre[0]== "J" or nombre[0]== "K" or nombre[0]== "L" or nombre[0]== "M":
        print("Usted perteneze al grupo A")
elif nombre[0]== "M":
    if nombre[0]== "N" or nombre[0]== "Ñ" or nombre[0]== "O" or nombre[0]== "P" or nombre[0]== "Q" or nombre[0]== "R" or nombre[0]== "S" or nombre[0]== "T" or nombre[0]== "V" or nombre[0]== "W" or nombre[0]== "X" or nombre[0]== "Y" or nombre[0]== "Z":
        print("Usted perteneze al grupo A")
else:
    print("Usted perteneze al grupo B")