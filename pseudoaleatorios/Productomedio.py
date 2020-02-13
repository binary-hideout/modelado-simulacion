def generador(semilla1, semilla2):
    """
    Funcion generador, recibe 2 parametros (semilla1, semilla2) y produce un valor
    utilizando el metodo de productos medios.
    """
    # Primero se realiza la multiplicacion con las dos semillas.
    resultado_semillas = semilla1 * semilla2
    # El resultado de la multiplicacion se convierte a un tipo de dato 'string'.
    resultado_semillas = str(resultado_semillas)
    # Con esta 'string' podemos encontrar cuantos digitos tiene nuestro numero.
    if (len(resultado_semillas) % 2 == 0):
        # Si nuestro numero contiene un numero par de digitos entonces llamar la funcion producto_medio.
        valor = producto_medio(resultado_semillas)
    else:
        # De lo contrario nuestro resultado debe tener una cantidad de digitos par, 
        # a este le agregamos un '0' a la izquierda,
        # de tal manera que no afecte el valor numerico.
        valor = '0' + resultado_semillas
        # Por ultimo, se manda a llamar la funcion de producto medio.
        valor = producto_medio(resultado_semillas)
    return valor

def producto_medio(numero):
    """
    Funcion producto medio, recibe un parametro y retorna el resultado flotante de acuerdo al metodo
    de producto medio.
    """
    # Se utiliza el operador // 'floor division' para que la divison retorne un entero.
    division = len(numero) // 2
    # Se utiliza los 'slices' de python para obtener los digitos del centro del producto de las dos semillas.
    resultado = numero[division - 1:division + 1]
    # Convertimos nuestro resultado a tipo entero.
    resultado = int(resultado)
    # Dividimos nuestro resultado entre 100
    resultado /= 100
    return resultado

def numeros_pseudoaleatorios():
    """
    Funcion numeros pseudoaleatorios, esta funcion realiza las iteraciones de acuerdo a la cantidad
    de numeros pseudoaleatorios que deseen generarse.
    """
    cantidad = int(input("Ingresa la cantidad de numeros pseudoaleatorios que desea generar: "))
    semilla1 = int(input("Ingresa la primera semilla: "))
    semilla2 = int(input("Ingresa la segunda semilla: "))
    print("\nSemilla #1" + "      " + "Semilla #2" + "      " + "Resultado")
    # Ciclo 'for' que itera n veces.
    for i in range(cantidad):
        # Se manda a llamar la funcion generador de acuerdo a las 2 semillas proporcionadas.
        resultado = generador(semilla1, semilla2)
        # La primer semilla obtiene el valor de la segunda.
        semilla1 = semilla2
        # La segunda semilla obtiene el valor del resultado multiplicado por 100.
        semilla2 = int(resultado * 100)
        # Se imprimen los resultados.
        print(str(semilla1) + "              " + str(semilla2) + "              " + str(resultado))

numeros_pseudoaleatorios()