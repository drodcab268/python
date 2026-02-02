pers={}
continuar=""

while continuar != "No":
    dato = input("¿Qué dato quiere introducir? (Nombre/Drección/Correo...): ")
    info = input(dato + ": ")
    
    pers[dato] = info
    print(pers)
    
    continuar = input("¿Quieres añadir más información (Si/No)? ")