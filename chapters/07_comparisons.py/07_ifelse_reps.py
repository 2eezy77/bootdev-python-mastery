
def check_player_score(current_name, high_scorer, low_scorer):
    if current_name == high_scorer:
        return f"{current_name} is the high scorer"
    elif current_name == low_scorer:
        return f"{current_name} is the low scorer"
    else:
        return f"{current_name} is neither"

current_player = "isaac"
best_player_name = "isaac"
worst_player_name = "ben"
mod_player_name = "jake"

def main():
    checkBestPlayer = check_player_score(current_player, best_player_name, worst_player_name)
    print(checkBestPlayer)

main()