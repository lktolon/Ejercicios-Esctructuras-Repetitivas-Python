suma = 0
contador =0

n = int(input("Inserte un número para sumar. Inserte 0 para salir:"))
while num != 0:
	suma = suma + n
	contador = contador + 1
	
	n = int(input("Inserte un número para sumar. Inserte 0 para salir:"))

if contador > 0:
	media = suma / contador
else:
	media = 0

print("La suma total asciende a:", suma)
print("La media de los número es:", media)
