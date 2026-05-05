def test_player_status(player_power, enemy_defense):
    advantage, evenly_matched, disadvantage = False, False, False

    if player_power > enemy_defense:
        advantage = True
    elif player_power == enemy_defense:
        evenly_matched = True
    else:
        disadvantage = True
    
    return advantage, evenly_matched, disadvantage

def main():
    goku = 260
    master_roshi = 180

    test_goku_status = test_player_status(goku, master_roshi)
    print(test_goku_status)

main()
