dinero=input("Introduzca el dinero que tiene con este formato (ej. 27.35€): ")
dineroSplit=dinero.split("€")
eurosCents=dineroSplit[0].split(".")
print(f"Usted tiene {eurosCents[0]} euros y {eurosCents[1]} centimos")