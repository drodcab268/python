palabra=input("Introduzca una palabra: ")
listPalabra=list(palabra)

for x in range(len(listPalabra)-1,-1,-1):
    print(listPalabra[x])