primo = True

num = int(input("Número a comprobar:"))

for i in range(2, num):
	if num % i == 0:
		primo = False

if primo:
	print("El número es primo")
else:
	print("El número no es primo")

