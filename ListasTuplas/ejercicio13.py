muestra = input("Introduzca una muestra de números separados por comas: ")
muestra = muestra.split(",")

nums = len(muestra)
for x in range(nums):
    muestra[x] = int(muestra[x])

muestra = tuple(muestra)
suma1 = 0
suma2 = 0
for i in muestra:
    suma1 = suma1 + i
    suma2 = suma2 + x**2

media = suma1/nums
desv = (suma2/nums-media**2)**(1/2)

print("La media es", media, ", y la desviación típica es", desv)