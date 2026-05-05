def new_abilities(starting_power):
    fireball = starting_power + 100
    counter_kick = starting_power + 25
    head_butt = starting_power + 250
    return fireball, counter_kick, head_butt

def display_new_abilities(starting_power):
    upgrading_character = new_abilities(starting_power)
    display = f"displaying your new abilities: {upgrading_character}"
    return display

def main():
    print("Welcome soldier, you aren't in Kansas anymore. Here comes first enemy! Get ready to try those new abilities out")
    get_more = display_new_abilities(100)
    print(get_more)

main()