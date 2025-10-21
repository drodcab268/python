renta=int(input("Introduzca su renta anual: "))

if renta < 10000:
    print("Le corresponde un inpositivo del 5%")

elif renta >= 10000 and renta < 20000:
    print("Le corresponde un inpositivo del 15%")

elif renta >= 20000 and renta < 35000:
    print("Le corresponde un inpositivo del 20%")

elif renta >= 35000 and renta < 60000:
    print("Le corresponde un inpositivo del 30%")

elif renta >= 60000:
    print("Le corresponde un inpositivo del 45%")
