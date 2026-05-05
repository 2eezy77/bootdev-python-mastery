def found_check(items):
    found = False

    for item in items:
        if item == "phone":
            found = True
    print(found)

check_closet = [
    "wallet",
    "checker piece",
    "sock",
    "underwear",
    "phone"
]

find_wallet = found_check(check_closet)
