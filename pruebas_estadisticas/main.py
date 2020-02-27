'''
Módulo para mandar a llamar las funciones de la tarea de Pruebas estadísticas.
'''

import os
import pathlib

from questionary import text, select, Choice

from validaciones import is_valid_chi
import abajo_arriba
import frecuencias
from ruta import get_file_path

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

def main():
    '''
    Corre el programa de Pruebas estadísticas.
    '''
    # ruta del archivo CSV que usa el programa
    csv_file = pathlib.Path(get_file_path('Pruebas.csv'))
    # si no existe el archivo en el directorio
    if not csv_file.exists():
        print("Tiene que existir un archivo llamado 'Pruebas.csv' en el mismo directorio para usar el programa.")
        # salir del programa
        return

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

main()
print()
os.system('pause')
