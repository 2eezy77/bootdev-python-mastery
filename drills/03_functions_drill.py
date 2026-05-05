'''
From memory, write:
* A function with 2 parameters that returns their sum
* A function with a default parameter
* Call both and print the results
'''

def sum(a, b):
    return f"sum of a + b = {a + b}"

def full_name(first="first_name", last="last_name"):
    return f"Hello {first} {last}!! Glad you understand code ;)"

add_em = sum(2, 2)
name = full_name("monty", "isaac")

print(add_em)
print(name)
