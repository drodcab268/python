opcion=input("Es usted vegetarianov (si/no): ")

if opcion == "si":
    print("Elija solo un ingrediente!")
    vege=input("Ingredientes vegetarianos: Pimiento y tofu. ")
    print(f"Ingredientes en su pizza: Mozzarella, tomate y {vege}.")
else:
    print("Elija solo un ingrediente!")
    carni=input("Ingredientes no vegetarianos: Peperoni, Jamón y Salmón. ")
    print(f"Ingredientes en su pizza: Mozzarella, tomate y {carni}.")
