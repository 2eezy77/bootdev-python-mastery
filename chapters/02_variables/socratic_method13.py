player_1, attack_player_1, defend_player_1, player_1_health = "Jake", 100, -25, 100
player_2, attack_player_2, defend_player_2, player_2_health = "sensei", 50, -80, 250

print(f"{player_1} prepares his own attack which deals {attack_player_1} damage.")
print(f"In doing so, {player_2} the master of quick attacks, being faster, quickly attacks {player_1} and deals a blowing shot which causes {player_1} a heavy blow of {attack_player_2} damage.")
print(f"{player_1} now has {player_1_health - attack_player_2}")