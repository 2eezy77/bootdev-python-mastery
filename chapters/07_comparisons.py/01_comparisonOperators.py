
playerOne = 1503418561903 
playerTwo = 1503815690832

def compareValues(a,b):
    result = a >= b
    return result

who_won = compareValues(playerOne, playerTwo)
print(who_won)