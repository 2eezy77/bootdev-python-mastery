def canServeDrink(age, on_break, bar_open):
    if age < 21 or on_break or bar_open < 5 or bar_open > 10:
        return False
    else:
        return True

jake_age = 22
bartender_on_break = False
current_time = 9

def main():
    canJakeOpenATab = canServeDrink(jake_age, bartender_on_break, current_time)
    print(canJakeOpenATab)
main()