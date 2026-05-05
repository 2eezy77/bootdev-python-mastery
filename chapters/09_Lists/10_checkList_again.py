def checklist(test_list):
    bat_count = 0
    player_count = 0
    uniform_count = 0

    for i in range(0, len(test_list)):
        if test_list[i] == "bat":
            bat_count += 1
        elif test_list[i] == "player":
            player_count += 1
        elif test_list[i] == "uniform":
            uniform_count += 1
    print(f"bat's:{bat_count}, player's:{player_count}, uniform:{uniform_count}")

list_team_items = [
    "bat",
    "bat",
    "player",
    "uniform",
    "uniform",
    "player",
    "player",
    "bat",
    "uniform"
]

check_team = checklist(list_team_items)


            