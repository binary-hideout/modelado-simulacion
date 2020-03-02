import math
import random

def poisson():
    lambda_value = 2.45
    constante = math.exp(-lambda_value)
    vp = 0
    x = 0
    suma = 0
    aleatorio = random.random()
    while suma <= aleatorio:
        if x == 0:
            pois = (constante * (lambda_value ** x))
        else:
            pois = (constante * (lambda_value ** x)) / math.factorial(x)
        suma += pois
        vp = x
        x += 1

    if vp == 0:
        vp = 1

    return vp
