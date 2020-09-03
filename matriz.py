# import libraries
from pandas import  *
import time
import os
#  function to create matriz

matriz = []
def create_matriz(width_m, length_m):
	for x in range(width_m):
		col = []
		for y in range(length_m):
			col.append(0)
		matriz.append(col)

x = int( input())
y = int( input())

create_matriz(x,y)
print('puntos'+str(x*y))

for j in range(x):
	for i in range(y):
		if(j%2==0):
			matriz[j][i]='x'
		else :
			matriz[j][y-i-1]='x' 
		print(DataFrame(matriz))
		time.sleep(0.5)
		input()
		os.system('clear')


