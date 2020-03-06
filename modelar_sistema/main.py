'''
Módulo para ejecutar tarea.
'''

from questionary import text

from validaciones import is_valid_time
from poisson import poisson

tl = text(
    'Ingresar límite de tiempo: ',
    validate=lambda s: True if is_valid_time(s) else 'Por favor ingrese un valor válido.',
    qmark='>'
).ask()

TLimite = float(tl)
LCajas = 30
TAsigC = 60
Ret = False
Reloj = 0
TC = 0

Ts1 = poisson()
Ts2 = poisson()

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

