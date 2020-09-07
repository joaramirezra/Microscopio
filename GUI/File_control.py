import os
def init_document(name):
    try :
        pwd = 'rm '+ name+'.csv'

    except:
        file1 = open(name +".csv","w+") 
    print(file1 + " open sucessfully"  )

