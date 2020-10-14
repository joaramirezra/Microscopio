# file managment functions 

#-------------------------------------------------------------------------------        
def clean_file():
	file = open("compuestos.csv","w") 
	file.close() 

#-------------------------------------------------------------------------------        
def create_title():
	file = open("compuestos.csv","w") 
	str_to_append = ";".join(["Point","Step" ,"Coor x" , "Coor y", 
							  "Component", "Size"])
	file.write((str_to_append+' \n'))
	file.close() 

#-------------------------------------------------------------------------------
def is_empty():
	try:
		file = open("compuestos.csv","r") 
	except:
		create_title()
		file = open("compuestos.csv","r")
	lines = file.readlines()
	return bool((len(lines)) <=1 )

#-------------------------------------------------------------------------------
def number_components():
	file = open("compuestos.csv","r") 
	lines = file.readlines()
	return (len(lines))

#-------------------------------------------------------------------------------
def add_point_to_file(point, step,coor_x , coor_y, element, size):
	str_to_append = ";".join([str(point),str(step), str(coor_x) , str(coor_y), 
							  str(element), str(size)])
	file = open("compuestos.csv","a")
	file.write(str_to_append+'\n')

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
		if(last[3].isnumeric() and last[1].isnumeric() and last[2].isnumeric()):
			return last
		else: 
			print("format error")
			return False
	else:
		print("size error")
		return False
