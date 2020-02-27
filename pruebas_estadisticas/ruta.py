'''
Módulo para obtener rutas físicas.
'''

import sys, os

def get_file_path(file_name):
    '''
    Regresa la ruta del archivo del argumento.
    '''
    # se está usando un .exe
    if getattr(sys, 'frozen', False):
        directory = os.path.dirname(sys.executable)
    # se está ejecutando el script
    else:
        directory = os.path.dirname(__file__)
    return os.path.join(directory, file_name)
