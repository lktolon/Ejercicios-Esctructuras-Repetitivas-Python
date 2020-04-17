x = int(input("Base de la potencia:"))

while True:
	exp = int(input("Exponente de la potencia:"))
	if exp<0:
		print("El exponente debe ser un número positivo")
	if exp >= 0:
		break;

total = 1

for i in range(1, exp + 1):
	total = total * x
print("La potencia es:", total)

