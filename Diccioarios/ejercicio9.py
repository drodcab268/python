factura={}
cobrado=0
pendiente=0
continua=""

while continua != "T":

    if continua == "A":
        num_fac = input("Introduzca el número de la factura: ")
        coste = float(input("Introduzca el coste de la factura: "))
        factura[num_fac] = coste
        pendiente += coste

    if continua == "P":
        clave = input("Introduzca el número de la factura a pagar: ")
        coste = factura.pop(clave, 0)
        cobrado += coste
        pendiente -= coste

    print(f"Recaudado: {cobrado}")
    print(f"Pendiente de cobro: {pendiente}")
    continua = input("¿Que quiere hacer? (añadir una nueva factura 'A', pagarla 'P' o terminar 'T'): ")
