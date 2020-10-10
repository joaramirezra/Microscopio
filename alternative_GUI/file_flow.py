# file managment functions 

#-------------------------------------------------------------------------------        
def clean_file():
	file = open("compuestos.csv","w") 
	file.close() 

#-------------------------------------------------------------------------------        
def create_file():
	file = open("compuestos.csv","w") 
	str_to_append = ";".join(["point", "coor x" , "coor y", 
							  "element", "size",'\n'])
	file.write(str_to_append)
	file.close() 

#-------------------------------------------------------------------------------
def numer_of_components():
	file = open("compuestos.csv","r") 
	lines = file.readlines()
	print(len(lines)-2)

#-------------------------------------------------------------------------------
def add_point_to_file(point, coor_x , coor_y, element, size):
	str_to_append = ";".join([str(point), str(coor_x) , str(coor_y), 
							  str(element), str(size),'\n'])
	file = open("compuestos.csv","a")
	file.write(str_to_append)

#-------------------------------------------------------------------------------
def Read_last_line():
	file = open("compuestos.csv","r")
	lines = file.readlines()
	
	if(len(lines)<2):
		print("Empty file error")	
		return False
	else :
		last = lines[len(lines)-1].split(";")
	
	if(len(last) == 6):
		if(last[0].isnumeric() and last[1].isnumeric() and last[2].isnumeric()):
			print(last)
		else: 
			print("format error")
			return False
	else:
		print("size error")
		return False
