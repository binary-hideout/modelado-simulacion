'''
Módulo para mandar a llamar las funciones de la tarea de Pruebas estadísticas.
'''

from questionary import text, select, Choice

from validaciones import is_valid_chi
import abajo_arriba
import frecuencias

menu = select(
    'Seleccione la prueba estadística a usar:',
    [
        Choice('Abajo y arriba', 1),
        Choice('Frecuencias', 2),
        Choice('Salir', 0)
    ],
    qmark='*'
).ask()

# abajo y arriba
if menu == 1:
    chi = text(
        'Ingrese valor para chi cuadrada:',
        validate=is_valid_chi,
        qmark='>'
    ).ask()
    abajo_arriba.inicio(float(chi))
# frecuencias
elif menu == 2:
    #! error
    frecuencias.main()
