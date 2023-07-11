# scracth_pad.py

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

def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    del my_list_1[0]  # Pay attention to this line.
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)


my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)


dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval", "fish": "poison"}

for key, value in dictionary.items():     # returns a key value pair as a tuple
    print(key, value)

for key in dictionary.keys():       # returns all keys in dictionary
    print(key)

for value in dictionary.values():   # returns all value in dictionary
    print(value)

dictionary["cat"] = "minou"         # replace value associated with cat key
print(dictionary)

dictionary["swan"] = "cygne"        # add new key / value (not recommended)
print(dictionary)

dictionary.update({"duck": "canard"})       # recommended way of adding new key / value
print(dictionary)

del dictionary["cat"]               # delete dict key / value
print(dictionary)

dictionary.popitem()                # delete last key / value in dictionary
print(dictionary)

new_dict = dictionary.copy()        # duplicate a dictionary
print(new_dict)

dictionary.clear()                  # clear dictionary
print(dictionary)

my_tuple = tuple(new_dict)          # convert dictionary to tuple
print(my_tuple)

colours_tuple = (("red", "rouge"),("green", "verdi"),("black", "noir"))
colours_tuple = dict(colours_tuple)         # convert tuple to dict
print(colours_tuple)

school_class = {}

while True:
    name = input("Enter the student's name: ")
    if name == '':
        break

    score = int(input("Enter the student's score (0-10): "))
    if score not in range(0, 11):
        break

    if name in school_class:
        school_class[name] += (score,)
    else:
        school_class[name] = (score,)

for name in sorted(school_class.keys()):
    adding = 0
    counter = 0
    for score in school_class[name]:
        adding += score
        counter += 1
    print(name, ":", adding / counter)
