
from poisson import 
	poisson

TLimite = int(input('Inserte el limite de tiempo ->'))
LCajas = 30
TAsigC = 60
Ret = False

Ts1 = poisson()

Ts2 = poisson()

delta = Min(Ts1,Ts2)
Reloj = Reloj + delta
TC = TC + delta 

if TC >= TAsigC:
	TC = TC - TAsigC
	LCajas = LCajas + 30
	Ret = False
	if Fila2 != 0:
		LCajas = LCajas - Fila2
		Fila2 = 0