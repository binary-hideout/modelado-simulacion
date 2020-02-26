import pandas as pd
import math

def main():
    zn = float(input('Ingresa el valor de la chi cuadrada: '))
    binario = lectura()
    z = abajo_arriba(binario)
    print(z)

    if z < zn:
        print('No se rechaza que proviene de una distribución uniforme')
    else:
        print('No pasa la prueba de las corridas')



def lectura():
    leer = pd.read_csv(filepath_or_buffer = "Pruebas.csv", header = None)
    datos = leer.values.ravel()
    
    text = ""
    for i in range(len(datos) - 1):
        if datos[i] > datos[i + 1]:
            text = text + "0"
        else:
            text = text + "1"
    
    return text

def abajo_arriba(binario):
    corridas = 1
    x = binario[0]

    for i in range(len(binario)):
        if binario[i] == x:
            corridas += 1
            x = binario[i]

    media = (2 * (len(binario) - 1)) / 3
    varianza = (16 * media - 19) / 90
    z = abs((corridas - media) / math.sqrt(varianza))
    
    return z
