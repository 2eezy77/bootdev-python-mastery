#skipping negative primes making the output very clean and fast
for number in range(-5,5):
    if number < 0:
        continue
    print(f"{number} in prime is: {number ** 0.5}")

#Only outputting every 3 iterations of the for for loop; skipping all others with the use of counter
def only_third_number():
    counter = 0
    for level in range(1, 30):
        counter += 1
        if counter < 3:
            continue
        else:
            counter = 0
            print(f"You achieved level: {level}")

only_third_number()