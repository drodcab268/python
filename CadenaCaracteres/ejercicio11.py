produ=input("Inroduzca el nombre del producto: ")
preci=input("Introduzca el precio del producto: ")
numUni=input("Introduzca el número de unidades: ")

total=float(preci)*float(numUni)

print(f"Producto: {produ:08.2f} Precio: {preci:03d}€, Unidades: {numUni:010.2f}, Total: {total}€")