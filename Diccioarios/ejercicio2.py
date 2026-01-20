nombre=input("Introduzca su nombre: ")
edad=input("Introduzca su edad: ")
direccion=input("Introduzca su dirección: ")
telefono=input("Introduzca su nº de teléfono: ")
persona={"nombre": nombre,"edad": edad,"direccion": direccion,"telefono": telefono}
print(persona["nombre"], "tiene", persona["edad"], "años, vive en", persona["direccion"], "y su número de teléfono es", persona["telefono"])
