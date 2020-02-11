def generador(semilla1, semilla2):
    resultado = semilla1 * semilla2
    resultado = str(resultado)
    if (len(resultado) % 2 == 0):
        valor = producto_medio(resultado)
    else:
        valor = '0' + resultado
        valor = producto_medio(resultado)
    return valor

def producto_medio(numero):
    division = len(numero) // 2
    resultado = numero[division - 1:division + 1]
    resultado = int(resultado)
    resultado = resultado / 100
    return resultado

print(generador(12, 14))