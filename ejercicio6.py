n1 = int(input("Valor del primer número:"))
n2 = int(input("Valor del segundo número:"))

if n1 % 2 == 1:
	n1 = n1 + 1;
for i in range(n1, n2 + 1, 2):
		print(i," ",end="")
