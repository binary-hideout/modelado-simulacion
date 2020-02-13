"""
Módulo para la CLI (interfaz de línea de comandos)
"""
import questionary

from Productomedio import numeros_pseudoaleatorios
from Cuadrado_medio import cuadrado_medio
from mcml import mcml

def run():
    '''
    Ejecuta la CLI.
    '''
    option = questionary.select(
        '¿Cuál método desea probar?',
        [
            questionary.Choice(
                'Producto medio',
                1
            ),
            questionary.Choice(
                'Cuadrados medios',
                2
            ),
            questionary.Choice(
                'Método congruencial mixto o lineal',
                3
            )
        ]
    ).ask()

    if option == 1:
        numeros_pseudoaleatorios()
    elif option == 2:
        seed = questionary.text('Ingresa la semilla:').ask()
        random = cuadrado_medio(int(seed))
        print('Número aleatorio:', random)
    elif option == 3:
        n = int(input('Inserte el limite de numeros aleatorios a desear ->'))
        while True:
            mod = int(input('Inserte el valor del modulo ->'))
            print('Los siguientes valores deben cumplir con la condicion de ser menores al modulo')
            xi = int(input('Inserte el valor de la semilla ->'))
            a = int(input('Inserte el valor del multiplicador->'))
            c = int(input('Inserte el valor del incremento->'))

            if xi < 0 or xi > mod or a < 0 or  a > mod or c < 0 or c > mod or mod <=0 or n <= 0:
                print('Sus datos ingresados no concuerdan con el programa, intente de nuevo')
            else:
                mcml(n, mod, xi, a, c)
                break