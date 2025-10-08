fecha=input('Introduzca la fecha de hoy con el siguiente formato "dd/mm/aaaa": ')
fechaSplit=fecha.split("/")
print(f"Hoy es día {fechaSplit[0]}, del mes {fechaSplit[1]}. del año {fechaSplit[2]}")