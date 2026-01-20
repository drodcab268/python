frutas = {"Plátano":1.35,"Manzana":0.8,"Pera":0.85,"Naranja":0.7}
fruta = input("Qué fruta quiere? ").title()
kg = float(input("Kilos: "))
if fruta in frutas:
    print(kg, "kg de ", fruta, " son ", frutas[fruta]*kg, "€")
else: 
    print("Lo siento, la fruta", fruta, "no está disponible.")