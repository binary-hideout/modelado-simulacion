'''
Módulo para mandar a llamar las funciones de la tarea de Pruebas estadísticas.
'''

from questionary import text, select, Choice

import abajo_arriba

menu = select(
    'Seleccione la prueba estadística a usar:',
    [
        Choice('Abajo y arriba', 1),
        Choice('Frecuencias', 2),
        Choice('Salir', 0)
    ]
).ask()

# abajo y arriba
if menu == 1:
    abajo_arriba.main()
# frecuencias
elif menu == 2:
    pass
