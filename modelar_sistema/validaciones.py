'''
Módulo local para validar entradas de usuario.
'''

import sys

def is_valid_time(string):
    '''
    Valida que un string contenga un tiempo válido.
    '''
    try:
        number = float(string)
    except ValueError:
        return False
    else:
        if number > 0 and number < sys.float_info.max:
            return True
        else:
            return False
