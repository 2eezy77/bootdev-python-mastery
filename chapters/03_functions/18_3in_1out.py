def truck_upgrade(truck, turbo, lift):
    base_pricing = truck + 5500
    turbo_lift_added = turbo + lift
    final_price = turbo_lift_added + base_pricing
    return final_price

total_pricing = truck_upgrade(25000, 15000, 3500)
print(total_pricing)
