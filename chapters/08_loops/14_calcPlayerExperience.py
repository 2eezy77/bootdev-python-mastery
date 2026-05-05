# total xp acquired given current level where each level upgrade requires current_level * 5xp.
# lvl 1 = 0xp, lvl 2 requires lvl 1 * 5, lvl 3 requires lvl 3 * 5, ....
def player_experience_sofar(current_level):
    xp = 0
    for i in range(1, current_level):
        xp += i * 5
        print(f"xp acquired for level {i} is {xp}")
    return f"current xp acquired for level {current_level} = {xp}"

level = 8
total_xp = player_experience_sofar(level)
print(total_xp)


