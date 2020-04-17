ntrab = int(input("Total de trabajadores:"))
sueldo = float(input("Sueldo por hora de trabajo:"))

acumulacion = 0

for i in range(1, ntrab + 1):
	
	horastotal = 0
	
	dias = int(input("Dias totales de trabajo del trabajador %d ?:" % i))
	
	for x in range(1, dias + 1):
		
		horas = int(input("Horas totales tranajadas por el trabajador %d el día %d ?:" % (i, x)))
		
		horastotal = horastotal + horas
	
	print("El trabajador %d tiene un total de ingresos de %f" % (i,horastotal * sueldo))
	acumulacion = acumulacion + horastotal

print("El pago total a los %d trabajadores asciende a: %f" % (ntrab,acumulacion * sueldo))

