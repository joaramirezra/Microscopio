import os
os.system('rm elementos.csv')
file1 = open("elementos.csv","a") 

def leer_Valor():
	print("ingrese elemento")	
	Elemento = input()
	return Elemento

lista_elementos = []
conteo = []
conteo_Tamano = []


def inicializar_arreglo():
	#lista_elementos = []
	for x in range(26):
		lista_elementos.append('')
		conteo.append(0)
		conteo_Tamano.append(0)

def iniciarlizar_elementos():
	print("Ingrese compuesto a adicionar")
	nombre = input()	
	print("Ingrese letra a asociar para "+ nombre)
	letra = input()	
	print("Al elemento "+ nombre + " se asignara la letra " + letra)
	lista_elementos[ord(letra)-97]= nombre
		

def leer_valor():
	print('ingrese valor')	
	entrada0 = input()
	entrada = list(entrada0)
	letra = ord(entrada[0])-97
	print(letra)
	print(int(entrada[1]))	
	llevar_cuenta(letra,int(entrada[1]))
	file1.write(lista_elementos[letra]+";"+str( entrada[1])+"\n	") 
	print(lista_elementos[letra])

	
def llevar_cuenta(num,tam):
	conteo[num] = conteo[num]+1
	conteo_Tamano[tam] = conteo_Tamano[tam]+1 

if __name__ == "__main__":
	os.system('clear')
	inicializar_arreglo()	
	print(" Cuantos elementos desea Guardar ? ")
	numero_elementos = int(input())
	for item in range(numero_elementos): 
		iniciarlizar_elementos()
		os.system('clear')
	print(lista_elementos)
	print("cuantos puntos desea contar ? ")	
	nn =int(input())	
	for x in range(nn):
		leer_valor()
	print(conteo)
	file1.close()

	print(conteo_Tamano)																																																																																																																						
