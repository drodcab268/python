fecha=input('Introduzca la fecha de su nacimiento con el siguiente formato "dd/mm/aaaa": ')
fechaSplit=fecha.split("/")
print(f"Usted nació el día {fechaSplit[0]}, del mes {fechaSplit[1]}, del año {fechaSplit[2]}")