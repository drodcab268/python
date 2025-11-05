pwd="usuario1234"
password=" "

while pwd != password:
    password=input("Introduzca la contraseña del sistema: ")
    if pwd != password:
        print("Contraseña incorrecta, inténtelo de nuevo :(")

print("Contraseña correcta, accediendo al sistema :)")