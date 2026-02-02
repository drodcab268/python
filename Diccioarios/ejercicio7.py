cesta={}
continuar=""
coste = 0

while continuar != "No":
    produ = input("Introduzca un artículo: ")
    precio = float(input(f"Introduzca el precio de {produ}: "))
    cesta[produ] = precio
    continuar = input("¿Quiere añadir más artículos a su lista (Si/No)? ")

print("Lista de la compra:")
for produ, precio in cesta.items():
    print(precio, "\t", precio)
    coste += precio
print("Coste total: ", coste)