# Components logic 
from Files_management import there_is_component,add_pair_key_component
from Files_management import new_component_count,replace_pair_key_component
from Files_management import replace_component_count

def add_new_component(key,component):
    if(there_is_component(key)):
        print('already exists')
    else:
        add_pair_key_component(key,component)
        new_component_count(component)

def replace_component(key,component):
    if(there_is_component(key)):
        replace_pair_key_component(key,component)
        replace_component_count(key,component)
    else:
        add_new_component(key,component)

def fill_to_test():
    add_new_component('a','analsita')
    add_new_component('w','wolframio')
    add_new_component('f','feldespato')
    add_new_component('q','quarzo')

    