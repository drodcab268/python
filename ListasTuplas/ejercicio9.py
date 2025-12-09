palabra=input("Introduce una palabra: ")
vocales=['a', 'e', 'i', 'o', 'u']
for x in vocales: 
    num = 0
    for y in palabra: 
        if y == x:
            num += 1
    print("La vocal ",x," aparece ",num," veces")