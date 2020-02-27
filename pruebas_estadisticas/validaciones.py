'''
Módulo local para validar entradas de usuario.
'''

def is_number(string):
    '''
    Valida que un string contenga un número válido.
    '''
    try:
        float(string)
    except ValueError:
        return False
    else:
        return True
