# scracth_pad.py

# BMI Calculator for weight in KG or LBs and height in meters or feet & inches
def lbs_to_kgs(kgs):
    one_lbs = 0.45359237            # one lbs in KG
    value = kgs * one_lbs           # convert lbs to kg
    return float(value)             # return result


def ft_inches_to_cm(ft, inch):
    one_foot = 0.3048               # one foot in meters
    one_inch = 0.0254               # one inch in meters
    ft_met = one_foot * ft          # convert feet to meters
    in_met = one_inch * inch        # convert inches to meters
    value = ft_met + in_met         # add the two converted values
    return float(value)             # return result


def bmi(we, he):                # bmi takes in 2 args
    bmi_result = we / he ** 2   # arithmetic = weight / height ** 2
    return bmi_result           # return result


w = (input("Do you want to enter weight in lbs (L) or kgs (K)? Enter L or K: "))
# prompt to enter in lbs or kilos
w = w.lower()                   # convert to lower
if w == "l":                    # if l entered prompt to enter weight in lbs
    w = float(input("Enter weight in lbs: "))
    w = float(lbs_to_kgs(w))     # send weight to conversion func lbs_to_kg

elif w == "k":
    w = float(input("Enter weight in kgs: "))   # if k entered prompt for weight in kgs

h = input("Do you want to enter height in ft, inches (F) or in meters (M)? Enter F or M: ")
# prompt to enter in ft/inches or meters
h = h.lower()                   # convert to lower
if h == "f":                    # if f entered prompt to enter height in ft/inches
    h1 = float(input("Enter height feet: "))
    h2 = float(input("Enter height inches: "))
    h = float(ft_inches_to_cm(h1, h2))      # send ft/inches to ft_inches_to_cm func

elif h == "m":
    h = float(input("Enter height in meters: "))    # if m entered prompt for height in meters

print(bmi(w, h))            # bmi function call with returned values for w & h as inputs
