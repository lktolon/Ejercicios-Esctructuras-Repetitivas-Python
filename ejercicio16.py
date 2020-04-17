acumulacion = 0

ntrab = int(input("Total de trabajadores:"))
sueldo = float(input("Sueldo por hora de trabajo:"))

for i in range(1, ntrab + 1):
	
	horas = int(input("Total de horas trabajadas por el trabajador %d ?:" % i))
	acumulacion = acumulacion + horas
	
	print("El trabajador %d tiene un total de ingresos de %f" % (i, horas*sueldo))

print("El pago total a los %d trabajadores asciende a: %f" % (ntrab, acumulacion * sueldo))

