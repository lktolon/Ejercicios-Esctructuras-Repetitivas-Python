import math

while True:
    
    cantidad = int(input("Cantidad de números que desea que sean mostrados:"))
    if cantidadr>0: break

print("1 :  2")

cantidad2 = 1

n = 3

while cantidad2 < cantidad:
    
    esprimo = True 
    
    for i in range(3, int(math.sqrt(n)) + 1, 2): 
        if n % i == 0: 
            esprimo = False  

    if esprimo:
         cantidad2 = cantidad2 + 1
        print(cantidad2, ": ", n)
    
    n = n + 2 

