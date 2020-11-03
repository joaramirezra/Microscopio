# Components logic 
from Files_management import there_is_component,add_pair_key_component
from Files_management import new_component_count,replace_pair_key_component
from Files_management import replace_component_count

#-------------------------------------------------------------------------------        
def add_new_component(key,component):
    if(there_is_component(key)):
        return False
    else:
        add_pair_key_component(key,component)
        new_component_count(component)
        return True

def replace_components(key,component):
    if(there_is_component(key)):
        replace_pair_key_component(key,component)
        replace_component_count(key,component)
        return True
    else:
        add_new_component(key,component)
        return True
    
    return False

    