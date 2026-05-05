def player_health(health):
    
    if health <= 0:
        return "dead"
    elif health <= 100:
        return "still alive"
    else:
        return "Not valid, reload game...."
def main():
    ryan, jake = -1, 65

    check_health_ryan = player_health(ryan)
    check_health_jake = player_health(jake)
    print(check_health_ryan)
    print(check_health_jake)

main()    
    