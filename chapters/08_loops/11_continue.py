for number in range(-5, 5):
    if number < 0:
        continue
    print(f"your prime {number} is {number ** 0.5}")

level = 1

def every_third():
    counter = 0
    for i in range(1, 15):
        counter += 1
        if counter < 3:
            continue
        else:
            counter = 0
            print(i)
every_third()