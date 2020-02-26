import pandas as pd
import math

def main():
    leer = pd.read_csv(filepath_or_buffer = "Pruebas.csv", header = None)
    datos = leer.values.ravel()
    cont1 = 0
    cont2 = 0 
    cont3= 0 
    cont4= 0 
    cont5= 0
    for i in range(len(datos) - 1):
        if datos[i] >=0 and datos[i] <=0.2:
           cont1=+1
        elif datos [i] >0.2 and datos [i] <=0.4:
            cont2=+1
        elif datos[i] >0.4 and datos [i] <=0.6:
            cont3=+1
        elif datos[i]>0.6 and datos[i] <=0.8:
            cont4=+1
        elif datos[i]>0.8 and datos[i] <=1:
            cont5=+1
    frecEsp = 20;
    chi = float(input('Ingresa el valor de la chi cuadrada: '))
    tot = (1/frecEsp)((cont1-frecEsp)^2+(cont2-frecEsp)^2+(cont3-frecEsp)^2+(cont4-frecEsp)^2+(cont5-frecEsp)^2)
    print("Valor de X es"+tot)
    if tot < chi:
        print('Los numeros no pertenecen a una distribucion uniforme')
    else:
        print('Los numeros no pertenecen a una distribucion uniforme')
