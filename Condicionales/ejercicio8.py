puntos = float(input("Introduzca su puntuación: "))

if puntos == 0.0:
    print("Inaceptable, no recibirá beneficios!")
elif puntos == 0.4:
    print("Aceptable, recibirá un beneficio de: ", 2400*puntos,"€")
elif puntos >= 0.6:
    print("Aceptable, recibirá un beneficio de: ", 2400*puntos,"€")
else:
    print("Puntos insuficientes...")