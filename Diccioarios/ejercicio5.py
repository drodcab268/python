curso={"Matemáticas": 6, "Física": 4, "Química": 5}
total_cred = 0

for asig, cred in curso.items():
    print(asig, " tiene: ", cred, " créditos")
    total_cred += cred
    
print("Número total de créditos del curso: ", total_cred)