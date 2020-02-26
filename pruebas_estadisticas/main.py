'''
Módulo para mandar a llamar las funciones de la tarea de Pruebas estadísticas.
'''

from questionary import text, select, Choice

menu = select(
    'Seleccione la prueba estadística a usar:',
    [
        Choice('Abajo y arriba', 1),
        Choice('Frecuencias', 2),
        Choice('Salir', 0)
    ]
).ask()
