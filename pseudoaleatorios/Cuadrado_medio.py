import math

def cuadrado_medio(semilla):
    n_s = str(semilla)

    potencia = int(math.pow(semilla, 2))
    n_ns = str(potencia)

    p = len(n_ns)
    q = len(n_s)

    a = n_ns
    for i in n_ns:
        if p < (2 * q):
            a = "0" + a
        else:
            break
    
    x = q // 4
    if (q % 2) == 0:
        x = q // 2
    numero_aleatorio = int(a[x:(p - 2)])

    return numero_aleatorio


x = cuadrado_medio(368)
print(x)