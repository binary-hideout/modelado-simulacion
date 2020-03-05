'''
parte 3 de la simulación
'''
from poisson.py import poisson

if (Fila1 != 0) & (Fila2 <= 5):
    Ts2 = Ts2 - delta
    if Ts2 == 0:
        if LCajas == 0:
            Fila2 = Fila2 + 1
        else:
            LCajas = LCajas - 1
        Na2 = Na2 + 1
        Fila1 = Fila1 - 1
        Ts2 = poisson()
else:
    To2 = To2 + delta

if Fila1 <= 5:
    Ts1 = Ts1 - delta
    if Ts1 == 0:
        Fila1 = Fila1 + 1
        Na1 = Na1 + 1
        Ts1 = poisson()
else:
    To1 = To1 + delta

if (LCajas == 0) & (Fila1 > 5) & (Fila2 >5):
    Ret = True