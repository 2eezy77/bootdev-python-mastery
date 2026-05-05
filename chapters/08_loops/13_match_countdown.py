def match_countdown():
    for i in range(10, 0, -1):
        if i == 1:
            print(f"{i}...Fight!")
        else:
            print(f"{i}...")

match_countdown()