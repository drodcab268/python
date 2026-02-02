def fun_area_cir(rad):
    pi = 3.1415
    return pi*rad**2

def fun_volumen_cir(rad, alt):
    return fun_area_cir(rad)*alt

print(fun_volumen_cir(9,17))