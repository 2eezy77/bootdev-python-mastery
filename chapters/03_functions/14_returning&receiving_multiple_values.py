def warrior(fullname, power):
    title = f"{fullname} is a warrior"
    updated_power = power + 1
    return title, updated_power

cool_title, cool_power = warrior("Batman", 7)
print(f"{cool_title} with a power upgraded to {cool_power}")