'''
From memory, write:
* Floor division (//) and modulo (%)
* An in-place operator (+= or *=)
* A logical expression with and or or
'''
a = 4
b = 6

roundDown_div = b // a
print(roundDown_div)

remainder_value = b % a
print(remainder_value)

a += 1
print(a)

b *= 2
print(b)

def logical_expression(first, second):
    if first == 2 and second == 2:
        print(True)

logical_expression(2, 2)
