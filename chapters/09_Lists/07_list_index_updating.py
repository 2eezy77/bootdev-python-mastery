def list_update(list_to_update):
    if list_to_update[3] == "apple":
        list_to_update[3] = "avocado"
    return list_to_update

def main():
    guacomole_recipe = [
        "tomatoes",
        "chili",
        "salt",
        "apple",
        ]
    
    check_recipe = list_update(guacomole_recipe)
    print(check_recipe)

main()