import pandas as pd

def lectura():
    leer = pd.read_csv(filepath_or_buffer = "Pruebas.csv", header = None)
    datos = leer.values.ravel()
    
    text = ""
    for i in range(len(datos) - 1):
        if datos[i] > datos[i + 1]:
            text = text + "0"
        else:
            text = text + "1"
    
    print(text)

lectura()