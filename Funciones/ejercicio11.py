def frecuencia (frase):
    div=frase.split(" ")
    dic={}
    for i in div:
        if i in dic:
            dic[i] +=1
        else:
            dic[i] =1
    return dic

frase = input(("Introduzca una frase: "))
print (frecuencia(frase))

def repeticion(dic):
    max_pala = ''
    max_frec = 0
    for i,h in dic.items():
        if h > max_frec:
            max_frec = h
            max_pala = i
    return max_pala, max_frec

print(repeticion(frecuencia(frase)))