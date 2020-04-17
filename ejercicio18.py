import os
import time

for h in range(0,24):
	
	for min in range(0,60):
		
		for seg in range(0,60):
			
			os.system("clear")
			
			print(h,":",min,":",seg)
			time.sleep(1)
