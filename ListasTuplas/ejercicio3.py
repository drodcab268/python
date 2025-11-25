asignaturas=["Matemáticas","Física","Química","Historia","Lengua"]
notas=[]

for asignatura in asignaturas:
    inNota=int(input(f"Introduzca la nota que ha sacado en {asignatura}: "))
    notas.append(inNota)

for i in range(len(asignaturas)):
    print(f"En {asignaturas[i]} ha sacado: {notas[i]}")