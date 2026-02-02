def mostrarDic(dic):
    for op, op2 in dic.items():
        print (op, op2)
       #print (dic.item())

dic = {'hello':'hola'}
option = 0

while option != 7:
    print("1. Mostrar diccionario")
    print("2. Añadir un elemento al diccionario")
    print("3. Actualizar un elemento del diccionario")
    print("4. Borrar un elemento del diccionario")
    print("5. Mostrar solo las claves")
    print("6. Mostrar solo los valores")
    print("7. Salir")
    option = int(input("Opción: "))

    if option == 1:
        mostrarDic(dic)

    elif option == 2:
        ing =input("Palabra en ingles: ")
        esp =input("Palabra en español: ")
        dic[ing] = esp
    
    elif option == 3:
        update = input("Introduzca la palabra a actualizar: ")
        new = input("Introduzca la palabra nueva: ")

        dic[update] = new

    elif option == 4:
        delete = input("Introduzca la palabra que quiera borrar: ")
        del dic[delete]

    elif option == 5:
        for op in dic.keys():
            print(op)

    elif option == 6:
        for op in dic.values():
            def mostrarDic(dic):
                for op, op2 in dic.items():
                    print(op, op2)

            dic = {'hello':'hola'}
            option = 0

            while option != 7:
                print("1. Mostrar diccionario")
                print("2. Añadir un elemento al diccionario")
                print("3. Actualizar un elemento del diccionario")
                print("4. Borrar un elemento del diccionario")
                print("5. Mostrar solo las claves")
                print("6. Mostrar solo los valores")
                print("7. Salir")
                option = int(input("Opción: "))

                if option == 1:
                    mostrarDic(dic)

                elif option == 2:
                    ing = input("Palabra en ingles: ")
                    esp = input("Palabra en español: ")
                    dic[ing] = esp
                
                elif option == 3:
                    update = input("Introduzca la palabra a actualizar: ")
                    new = input("Introduzca la palabra nueva: ")
                    dic[update] = new

                elif option == 4:
                    delete = input("Introduzca la palabra que quiera borrar: ")
                    del dic[delete]

                elif option == 5:
                    for op in dic.keys():
                        print(op)

                elif option == 6:
                    for op in dic.values():
                        print(op)