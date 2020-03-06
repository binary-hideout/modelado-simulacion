'''
Módulo para ejecutar tarea.
'''

from os import system

from questionary import text

from validaciones import is_valid_time
from poisson import poisson

tl = text(
    'Ingresar límite de tiempo:',
    validate=lambda s: True if is_valid_time(s) else 'Por favor ingrese un valor válido.',
    qmark='>'
).ask()

TLimite = float(tl)
LCajas = 30
Na1 = 0
Na2 = 0
TAsigC = 60
Ret = False
Reloj = 0
TC = 0
To1 = 0
To2 = 0
Fila1 = 0
Fila2 = 0

Ts1 = poisson()
Ts2 = poisson()

while True:
	delta = min(Ts1, Ts2)

	Reloj += delta
	TC += delta 

	if TC >= TAsigC:
		TC = TC - TAsigC
		LCajas = LCajas + 30
		Ret = False
		if Fila2 != 0:
			LCajas = LCajas - Fila2
			Fila2 = 0

	if Ret == True:
		NumRet = NumRet + 1
		ToFaltaCajas = ToFaltaCajas + (TAsigC-TC)
		To1 = To1 + (TAsigC-TC)
		To2 = To2 + (TAsigC-TC)
		Reloj = Reloj + (TAsigC-TC)
		TC = TAsigC
	else:
		#parte 3 
		if (Fila1 != 0) and (Fila2 <= 5):
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

		if (LCajas == 0) and (Fila1 > 5) and (Fila2 >5):
			Ret = True
			#salida 4
	if Reloj >= TLimite:
		break

print('Tiempo de ocio de la estación 1: %d' % To1)
print('Tiempo de ocio de la estación 2: %d' % To2)
print('Ejes atendidos de la estación 1: %d' % Na1)
print('Ejes atendidos de la estación 2: %d' % Na2)

print()
system('pause')
