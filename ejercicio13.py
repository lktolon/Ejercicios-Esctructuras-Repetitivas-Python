acumulacion = 0

shora = float(input("Sueldo pagado por hora:"))

for i in range(1, 7):
	h = int(input("Horas trabajadas el día %d :" % dia))
	acumulacion = acumulacion + h

print("Total de horas acumuladas:",acumulacion)
print("Sueldo:",sueldo_por_hora*horas_acum)
