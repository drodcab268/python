correo=input("Introduzca su correo electronico: ")
correoSplit=correo.split("@")[0]
correoNuev=correoSplit + "@ceu.es"
print("Su nuevo correo es:", correoNuev)