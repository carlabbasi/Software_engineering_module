# Tue4Jul.py
import time                                                         # import time for LABs 3.2.1.3 & 3.2.1.6 

# 3.1.1.12 LAB - Leap year checker
# input
print("\nEnter a year to find out whether it is a common year or a leap year!")
year = int(input("Select a year: "))                                 # user inputs year

# year calculation
if year < 1582:                                                     # is year before 1582?
    print("This year is before the start of the Gregorian calendar")
else:
    if year % 4 != 0:                                               # is year dividable by 4?
        print("This is a common year")
    elif year % 100 != 0:                                           # is year dividable by 100?
        print("This is a leap year")
    elif year % 400 != 0:                                           # is year dividable by 400?
        print("This is a common year")
    else:                                                           # otherwise leap year.
        print("This is a leap year")
print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")


# 3.2.1.3 LAB - garry trotter secret number guesser

print("+================================+     ^")               # welcome message
time.sleep(0.25)
print("| Welcome to my game, muggle!    |    /_\\")
time.sleep(0.25)
print("| Enter an integer number        |     O  |")
time.sleep(0.25)
print("| and guess what number I've     |   --|--|")
time.sleep(0.25)
print("| picked for you.                |     |  |")
time.sleep(0.25)
print("| So, what is the secret number? |    / \\")
time.sleep(0.25)
print("+================================+   /   \\")
time.sleep(0.25)

secret_number = 777                                             # declare secret number
guesses = 1                                                     # total guesses variable
guess_lst = []                                                  # empty list to catch previous guesses
guess = int(input("\nEnter your guess: "))                      # number guess prompt

while guess != 777:                                             # while guess is not secret number enter loop
    print("Hmmm, thinking......")                               # calculating guess
    time.sleep(0.5)
    print(f"\nNope! You're stuck in my loop! You incorrectly guessed {guess}.")
    guesses += 1                                                # increment guesses by 1 after each guess
    guess_lst.append(guess)                                     # append last guess to guess list

    if "77" in str(guess):                                     # if "77" appears in guess at all, 2 numbers correct
        print("At least two of those digits are correct, keep guessing!")
        guess = int(input("Enter your guess: "))

    elif "7" in str(guess):                                      # if "7" appears in guess at all, 1 number correct
        print("At least one of those digits is correct, keep guessing!")
        guess = int(input("Enter your guess: "))

    else:
        guess = int(input("Enter your guess: "))

print(f"""
Well done, muggle! You are free now.
You guessed the secret number {guess} after {guesses} attempts.
Your previous guesses were {guess_lst}
""")
print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")


# 3.2.1.6 LAB - Count mississippily to five

print("\nCount mississippily to five.")
user = input("Ready to count? (Y/N): ")             # ask if user is ready to count
user = user.upper()                                 # convert user input to uppercase

while user != "Y":                                  # if user doesn't input Y, continue to ask until ready to count
    user = input("Ready to count now? (Y/N): ")
    user = user.upper()                             # convert user input to uppercase

for count in range(1, 6):                           # for loop from 1-5
    dot = "."                                       # define dot as "."
    dots = count * dot                              # for each iteration the count increases the amount of "."
    print(f"{count} Mississippi{dots}")             # output to screen count increments with same number of dots
    time.sleep(1)                                   # sleep for 1 second

print("\nReady or not, here I come!")               # on completion of loop print statement
print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
