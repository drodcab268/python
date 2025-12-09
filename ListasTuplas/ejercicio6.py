asignaturas=["Matemáticas","Física","Química","Historia","Lengua"]
repetir=[]

for asignatura in asignaturas:
    nota=int(input(f"Introduzca la nota que ha sacado en {asignatura}: "))
    
    if nota < 5:
        repetir.append(asignatura)

print()
print("Asignaturas que tienes que repetir:")
for x in repetir:
    print(x)