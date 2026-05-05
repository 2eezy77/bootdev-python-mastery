tobias_health, peters_health, anna_health = 100, 20, 75

def take_potion(player_health):
    if player_health <= 50:
        print("Your health is low, you can take a potion to begin regenerating")
        return
    print("You can't take potion with a health above 51; you're okay to keep pushing")
    return

check_player_one = take_potion(tobias_health)
check_player_two = take_potion(peters_health)
check_player_three = take_potion(anna_health)