
# 4.3.1.9 LAB - Prime number finder

def is_prime(num):

    for a in range(2, int(1 + num **0.5)):
        if num % a == 0:
            return False
    return True

for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()


# 4.3.1.10 LAB: Fuel consumption converter

def liters_100km_to_miles_gallon(liters):
    gallons = liters / 3.785411784
    miles = 100 * 1000 / 1609.344
    return miles / gallons


def miles_gallon_to_liters_100km(miles):
    km = miles * 1609.344 / 1000 / 100
    liters = 3.785411784
    return liters / km


print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))

print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
