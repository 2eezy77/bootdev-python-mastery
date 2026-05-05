def total_gas_cost(miles,mpg):
    result = (miles / mpg) * 3
    return result

florida_trip = total_gas_cost(200,30)
print(florida_trip)

nyc_trip = total_gas_cost(800, 15)
print(nyc_trip)