player_1 = 0b1000
player_2 = 0b0100
player_3 = 0b0010
player_4 = 0b0001
team1 = 15

def combine_permissions(player1, player2, player3, player4):
    bitwise_sum = player1 | player2 | player3 | player4
    return bitwise_sum

def main():
    team_1 = combine_permissions(player_1, player_2, player_3, player_4)
    print(team_1 == team1)

main()