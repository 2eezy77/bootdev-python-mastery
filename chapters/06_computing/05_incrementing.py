def incrementation(current_health, potion):
    current_health += potion
    return current_health

def main():
    print(incrementation(85, 15))

main()