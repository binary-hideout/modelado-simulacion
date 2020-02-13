def mcml(n, mod, x, a, c):
	x1 = x
	while n:
		R = ((a * x1) + c) % mod 
		x2 = R 
		R = R / mod
		print('Número aleatorio:', R)
		x1 = x2
		n -= 1
