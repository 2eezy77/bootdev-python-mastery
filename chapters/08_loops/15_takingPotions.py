# use 1:1 ratio to regenerate as long as health is under max and potions are available
def regenerate(health, max_health, available_potions):
    while health < max_health and available_potions > 0:
        health += 1
        available_potions -= 1
    return health, available_potions

regenerate_health = regenerate(0, 100, 85)
print(regenerate_health)