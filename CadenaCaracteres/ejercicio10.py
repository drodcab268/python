listaComp=input("Introduzca su lista de la compra separando todos los elementos con comas: ")
listaSplit=listaComp.split(",")
print("\n".join(listaSplit))

#Otra forma de hacerlo:
#listaComp=input("Introduzca su lista de la compra separando todos los elementos con comas: ")
#print(listaComp.replace(",","\n"))