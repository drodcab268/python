def fun_cuadr(list_num):
    list_cuadr=[]
    for i in list_num:
        list_cuadr.append(i**2)
    return list_cuadr

def fun_mvd(list_num):
    dic_mvd={}
    dic_mvd["media"] = sum(list_num)/len(list_num)
    dic_mvd["varianza"] = sum(fun_cuadr(list_num))/len(list_num)-dic_mvd["media"]**2
    dic_mvd["desviacion tipica"] = dic_mvd["varianza"]**0.5
    return dic_mvd

print(fun_mvd([7, 18, 23, 19, 11]))