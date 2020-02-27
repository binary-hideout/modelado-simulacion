'''
Módulo para mandar a llamar las funciones de la tarea de Pruebas estadísticas.
'''

from questionary import text, select, Choice

from validaciones import is_valid_chi
import abajo_arriba
import frecuencias

def read_chi():
    '''
    Pide al usuario ingresar un valor para chi cuadrada.
    '''
    chi = text(
        'Ingrese valor para chi cuadrada:',
        validate=is_valid_chi,
        qmark='>'
    ).ask()
    return float(chi)

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
    chi = read_chi()
    abajo_arriba.inicio(chi)
# frecuencias
elif menu == 2:
    chi = read_chi()
    frecuencias.main(chi)
