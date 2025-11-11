frase=input("Introduzca una frase por pantalla: ")
letra=input("Introduzca una letra que aparezca en la frase anterior: ")
listFrase=list(frase)

count=0
for x in range(0,len(frase)):
    if (frase[x]==letra):
       count=count+1
if (count==1):
    print(f"La letra: {letra}, ha aparecido {count} vez")
elif (count>1):
    print(f"La letra: {letra}, ha aparecido {count} veces")
else:
    print(f"La letra: {letra}, no aparece en la frase introducida")    
