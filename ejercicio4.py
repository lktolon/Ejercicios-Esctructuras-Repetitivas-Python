negativos = 0
positivos = 0
ceros = 0

cantnum=int(input("Cantidad de números que van a ser introducidos:"))

for i in range(1,cantnum + 1):
	
	print("Número ",i,":",end="");
	
	n=int(input())
	
	if n>0:
		positivos = positivos + 1
	else:
		if n<0:
			negativos = negativos + 1
		else:
			ceros = ceros + 1

print("Cantidad de números positivos introducidos:", positivos);
print("Cantidad de número negativos introducidos:", negativos);
print("Cantidad de ceros introducidos:", ceros);

