'''
From memory, write:
* A function that uses a variable defined inside it (local scope)
* A function that uses a variable defined outside it (global scope)
'''

def first_name(first):
    return first

hello = first_name("monty")

def welcome_statement():
    whoami = first_name(hello)
    return f"Welcome {whoami}, glad you are here, \nthis is a perfect example of scope, \nget the inside joke HAHAHAH!! \n oh sorry nvm "

hello_world = welcome_statement()
print(hello_world)