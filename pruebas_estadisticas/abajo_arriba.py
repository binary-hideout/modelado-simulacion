import csv
import os.path
import math

def inicio(zn): # Recibe la "chi cuadrada"
    z = lectura()
    binario = lectura()
    z = abajo_arriba(binario)
    print('Varianza: %g' % z)
    if z < zn:
        print('No se rechaza que proviene de una distribución uniforme')
    else:
        print('No pasa la prueba de las corridas')


def lectura():
    text = ""
    path = os.path.dirname(__file__)
    file_path = os.path.join(path, 'Pruebas.csv')
    with open(file_path, encoding='utf-8-sig') as pruebas:
        csv_reader = csv.reader(pruebas)
        datos = []
        for row in csv_reader:
            numbers = map(float, row)
            datos.extend(numbers)

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

inicio(4.5)