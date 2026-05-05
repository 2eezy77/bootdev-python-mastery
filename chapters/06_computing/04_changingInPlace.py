def changing_in_place(constant):
    constant = constant + 1
    return constant

updated_itself = changing_in_place(1)
print(updated_itself)