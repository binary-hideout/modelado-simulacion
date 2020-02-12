import math

def cuadrado_medio(semilla):
    n_s = str(semilla) # n -> cantidad de dígitos

    nueva_semilla = math.pow(semilla, 2)
    n_ns = str(nueva_semilla) # n -> cantidad de dígitos

    longitud = False
    num = ""
    while longitud != True:
        if (len(n_ns) < (2 * len(n_s))):
            num = "0" + n_s
        else:
            longitud = True
    
    x = math.floor(semilla / 2)
    y = (len(num) - 1)
    num_aleatorio = (num[x:y])

    return num_aleatorio

x = cuadrado_medio(300)
print(x)

"""
NO HACE NADA
"""
