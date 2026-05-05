def total_damage(main_attack, core_attack, counter_attack):
    sum = main_attack + core_attack + counter_attack
    return sum

slide_kick = total_damage(25, 50, 30)
captain_punch = total_damage(50, 100, 30)
killer_combo = total_damage(25, 25, 100)

print(slide_kick)
print(captain_punch)
print(killer_combo)
print("Total number of function calls: 3")