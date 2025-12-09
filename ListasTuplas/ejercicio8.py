palabra=input("Introduce una palabra: ")

palabra_rev=palabra[::-1]

if palabra == palabra_rev:
    print("Es un palíndromo")

else:
    print("No es un palíndromo")