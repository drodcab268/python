diccionario={}
palabras=input("Introduzca la lista de palabras y traducciones (en formato palabra:traducción,palabra:traducción...): ")

for i in palabras.split(","):
    esp, ing = i.split(":")
    diccionario[esp] = ing

frase = input("Introduzca una frase en español: ")

for i in frase.split():
    if i in diccionario:
        print(diccionario[i], end=" ")
    else:
        print(i, end=" ")