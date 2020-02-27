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

def is_valid_chi(string):
    '''
    Valida que un string sea una chi cuadrada válida.
    '''
    if is_number(string):
        chi = float(string)
        if chi > 0:
            return True
    return 'Por favor ingrese un valor válido.'
