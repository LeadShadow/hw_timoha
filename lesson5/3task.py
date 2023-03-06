base_rate = 40 # базовий тариф
price_per_km = 10  # ціна за 1 км
total_trip = 0  # кількість поїздок


def trip_price(path):
    global total_trip
    total_trip += 1
    sum = base_rate + price_per_km * path
    return sum


print(trip_price(5))
print(total_trip)
print(trip_price(4))
print(total_trip)
