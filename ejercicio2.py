import random

x = 10;

nsec  =  random.randint(1,100);
num = int(input("Adivina el número:"))

while nsec != num and x>1:
    if nsec > num:
        print("Por debajo del número")
    else: 
        print("Por encima del número")
    intentos  =  intentos-1;
    
    print("Quedan ",intentos," intentos:")
    num = int(input("Adivina el número:"))

if nsec == num:
    print("Correcto, lo adivino en:", 11-intentos," intentos.")
else:
    print("Sin intentos, el número secreto era: ",nsec)

