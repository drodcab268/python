numero=int(input("Cuántos números de la loteria va a introducir? "))

loteria=[]

for x in range(numero):
    num=int(input('Introduzca los números de la loteria ("0" para salir): '))
    loteria.append(num)
    
loteria.sort()
for numLoteria in loteria:
    print(numLoteria)