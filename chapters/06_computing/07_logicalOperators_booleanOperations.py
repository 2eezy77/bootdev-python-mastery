def boolean_operators():
    a = True
    b = False
    valid = a and a
    still_valid = a or b
    not_valid = a and b
    still_not_valid = b or b
    nested_valid = (a or b) and a
    nested_not_valid = (a and b)or(b or b)
    return valid, still_valid, not_valid, still_not_valid, nested_valid, nested_not_valid

print(boolean_operators())