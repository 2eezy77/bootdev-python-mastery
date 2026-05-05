def main():
    print("This is main running. :)")

def total_price(tire1, tire2, tire3, tire4):
    sum = tire1 + tire2 + tire3 + tire4
    return sum

def annual_oil_avg(a, b, c, dd):
    avg = (a + b + c + dd) / 4
    return avg



tire_purchase = total_price(200, 300, 250, 400)
print(tire_purchase)

annual_oilchanges = annual_oil_avg(65, 70, 85, 75)
print(annual_oilchanges)

print(f"Tires are insanely expensive, total price for 4 tires is ${tire_purchase}. 2025, I spent, on average, ${annual_oilchanges} on oil changes. This car might have to get sold :/.")
main()