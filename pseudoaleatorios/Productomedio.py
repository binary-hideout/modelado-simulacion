def generador(semilla1, semilla2):
    resultado_semillas = semilla1 * semilla2
    resultado_semillas = str(resultado_semillas)
    if (len(resultado_semillas) % 2 == 0):
        valor = producto_medio(resultado_semillas)
    else:
        valor = '0' + resultado_semillas
        valor = producto_medio(resultado_semillas)
    return valor

def producto_medio(numero):
    division = len(numero) // 2
    resultado = numero[division - 1:division + 1]
    resultado = int(resultado)
    resultado = resultado / 100
    return resultado

def numeros_pseudoaleatorios():
    cantidad = int(input("Ingresa la cantidad de numeros pseudoaleatorios que desea generar: "))
    semilla1 = int(input("Ingresa la primera semilla: "))
    semilla2 = int(input("Ingresa la segunda semilla: "))
    for i in range(cantidad):
        resultado = generador(semilla1, semilla2)
        semilla1 = semilla2
        semilla2 = int(resultado * 100)
        print(resultado)

numeros_pseudoaleatorios()