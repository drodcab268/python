def fun_cuadrado(list_nums):
    list_cuad=[]
    for i in list_nums:
        list_cuad.append(i**2)
    return list_cuad

print(fun_cuadrado([7, 4, 28, 15, 17]))