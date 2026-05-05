

def fruit_types(fruit_list):
    apple_count = 0    
    banana_count = 0
    orange_count = 0

    for fruit in range(0, len(fruit_list)):
        if fruit_list[fruit] == "apple":
            apple_count += 1
        elif fruit_list[fruit] == "banana":
            banana_count += 1
        elif fruit_list[fruit] == "orange":
            orange_count += 1
    return apple_count, banana_count, orange_count
def main():
    fruits = [
        "apple",
        "banana",
        "orange",
        "apple",
        "orange"
    ]   

    get_fruits = fruit_types(fruits)
    
    print(get_fruits)

main()