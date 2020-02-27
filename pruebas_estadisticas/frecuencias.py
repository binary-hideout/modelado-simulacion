import csv
import os.path

def main(chi):
    cont1 = 0
    cont2 = 0 
    cont3= 0 
    cont4= 0 
    cont5= 0
    tot = 0
    path = os.path.dirname(__file__)
    file_path = os.path.join(path, 'Pruebas.csv')
    with open(file_path, encoding='utf-8-sig') as pruebas:
        csv_reader = csv.reader(pruebas)
        datos = []
        for row in csv_reader:
            numbers = map(float, row)
            datos.extend(numbers)
    for i in range(len(datos) - 1):
        if datos[i] >=0 and datos[i] <=0.2:
           cont1+=1
        elif datos [i] >0.2 and datos [i] <=0.4:
            cont2+=1
        elif datos[i] >0.4 and datos [i] <=0.6:
            cont3+=1
        elif datos[i]>0.6 and datos[i] <=0.8:
            cont4+=1
        elif datos[i]>0.8 and datos[i] <=1:
            cont5+=1
    frecEsp = 20
    print('Frecuencia observada')
    print(cont1, cont2, cont3, cont4, cont5)
    tot = ((1/frecEsp)*((cont1-frecEsp)**2+(cont2-frecEsp)**2+(cont3-frecEsp)**2+(cont4-frecEsp)**2+(cont5-frecEsp)**2))
    print("Valor de X es", tot)
    if tot < chi:
        print('Los numeros pertenecen a una distribucion uniforme')
    else:
        print('Los numeros no pertenecen a una distribucion uniforme')
