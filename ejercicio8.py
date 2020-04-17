sum = 0
fuera = 0
igual = False

while True:
	linferior = int(input("Límite inferior del intervalo"))
	lsuperior = int(input("Límite superior del intervalo:"))
	
	if linferior>lsuperior:
		
		print("El límite inferior debe ser menor que el límite superior")
	
	if linferior<=lsuperior:
		
		break;

n= int(input("Inserte un número o inserte 0 para terminar el programa:"))

while num !=0:

	if n>linferior and n<lsuperior:
		suma = suma + n
	else:
		# No pertenece al intervalo
		fuera = fuera + 1
	
	if n == linferior or n == lsuperior:
		igual = True
	
	n = int(input("Inserte un número o inserte 0 para terminar el programa:"))

print("La suma total es: ",suma_dentro_intervalo)
print("La cantidad total de números que estan fuera es de:",cont_fuera_intervalo)

if igual:
	print("Se ha introducido un número similar a los límites del intervalo")
else:
	print("No se ha introducido un número similar a los límites del intervalo")
