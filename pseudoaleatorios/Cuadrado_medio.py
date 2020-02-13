import math

def cuadrado_medio(semilla):
    n_s = str(semilla) # n -> cantidad de dígitos

    nueva_semilla = math.pow(semilla, 2)
    nueva_semilla = int(nueva_semilla)
    n_ns = str(nueva_semilla) # n -> cantidad de dígitos
    longitud = 1
    num = n_ns
    while longitud:
        if (len(num) < (2 * len(n_ns))):
            num = "0" + num
        else:
            longitud = 0
    x = len(num) // 2
    num_aleatorio = num[x - 2: x + 2]
    num_aleatorio = float(num_aleatorio)
    num_aleatorio /= 100

    return num_aleatorio
