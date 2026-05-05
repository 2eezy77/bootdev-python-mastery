def add(a, b):
    return a + b

'''displaying how scope works'''
def main():
    #cant use a because a is only visible within add() 
    #cant use b because b is only visible within add() 
    adding_values = add(1, 2)
    print(f"Your values added are: {adding_values}")

main()  