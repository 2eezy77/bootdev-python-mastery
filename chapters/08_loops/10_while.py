#you can regenerate as long as the enemy isn't within 3 meters, and your current_health is less than your max_health
def can_regenerate(current_health, max_health, enemy_distance):
    while current_health < max_health and enemy_distance > 3:
        current_health += 1
        enemy_distance -= 2
        print(f"current health: {current_health}")
        print(f"enemy distance: {enemy_distance}")
    return f"total health after regenerating: {current_health}" 

health_rn = 25
health_full = 100
enemy_from_me = 75

test_regenerate = can_regenerate(health_rn, health_full, enemy_from_me)
print(test_regenerate)
