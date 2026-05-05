def multiply_by_four(a):
    result = a * 4
    print("Print will print to console and return, unless printed() later after returned to caller will not print to console.")
    return result

value_multiplied_by_four = multiply_by_four(2)
print(f"This prints 2 multiplied by 4 which is {value_multiplied_by_four}")
