# this file helps to manage some files

# Create file 

def create_file(reference):
	files = ["mov_parameters.csv","count_parameters.csv","components.csv",
			 "size-count.csv","compenents-count.csv"]

	file = open(files[reference],"w") 
	
	if (reference == 0):
		parameters = ["connection_status","port_name","step","speed"]
		[file.write(":".join([param,"0"]) + '\n' ) for param in parameters]

	elif (reference == 1):
		parameters = ["max_count","step","counter","coor_x","coor_y"]
		[file.write(":".join([param,"0"]) + '\n' ) for param in parameters]

	elif (reference == 2):
		tittle = ";".join(["count" ,"coor x" , "coor y","Component", "Size"])
		file.write((tittle+' \n'))

	elif (reference == 3):
		sizes = ["<1e-3","2e-3","5e-3","0.01","0.02","0.05","0.1","0.25","0.2",
			   "0.5","1","2","3","5","10","20",">20"]
		[file.write(":".join([size,"0"]) + '\n' ) for size in sizes]

	file.close() 

def change_mov_parameters(status,portname,step,speed):
	file = open("mov_parameters.csv","w")
	
	status = True if (status=="1") else False
	parameters = ["connection_status","port_name","step","speed"]
	values = [str(status),str(portname),str(step),str(speed)] 
	
	[file.write(":".join([parameters[i],values[i]]) + '\n' ) for i in range(4)]
	file.close()

def change_count_parameters(max_count,step,counter,coor_x,coor_y):
	file = open("count_parameters.csv","w")
	
	parameters = ["max_count","step","counter","coor_x","coor_y"]
	values = [str(max_count),str(step),str(counter),str(coor_x),str(coor_y)] 
	
	[file.write(":".join([parameters[i],values[i]]) + '\n' ) for i in range(4)]
	file.close()

def add_components(count ,coor_x ,coor_y,Component, Size):
	file = open("components.csv","a")
	
	values = [str(count),str(coor_x),str(coor_y),str(Component),str(Size)] 
	
	[file.write((",".join([value for value in values])+ str('\n')))]
	file.close()


[add_components(1,1,k,1,1) for k in range(50)] 