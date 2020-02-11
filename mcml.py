import sys
 
 
try: 
	n = int(input('Inserte el limite de numeros aleatorios a desear ->'))
	mod = int(input('Inserte el valor del modulo ->'))
	print('Los siguientes valores deben cumplir con la condicion de ser menores al modulo')
	xi = int(input('Inserte el valor de la semilla ->'))
	a = int(input('Inserte el valor del multiplicador->'))
	c = int(input('Inserte el valor del incremento->'))
 
	if xi < 0 or xi > mod or a < 0 or  a > mod or c < 0 or c > mod or mod <=0 or n <= 0:
		raise Exception('Sus datos ingresados no concuerdan con el programa, intente de nuevo')
	 
	for i in  range(0,n):
		R =((a*xi)+c) % mod 
		xi = R 
		R = R/mod 
		print(R)
		
	input()
except ValueError as err:
	print('Error: {}'.format(err))
	sys.exit()

except Exception as miss:
	print('Salió otro error: {}'.format(miss))
	sys.exit()
	
 