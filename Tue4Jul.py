# Tue4Jul.py

import time             # import time module for LABs 3.2.1.3 & 3.2.1.6 (modules should be imported at start of file)

# 3.1.1.12 LAB - Leap year checker
# input
print("\nEnter a year to find out whether it is a common year or a leap year!")
year = int(input("Select a year: "))                                # user inputs year

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


# 3.2.1.3 LAB -  secret number guessing game
# print "animated" welcome message
print("\n+================================+              ^       _________________")
time.sleep(0.5)                                                                         # add delay for animate effect
print("| Enter an integer number        |         o   /_\\     / Welcome muggle! \\")
time.sleep(0.5)
print("| to guess my secret number.     |         |    O    <%\\_________________/")
time.sleep(0.5)
print("| Guess correctly to win a       |         | ---|---")
time.sleep(0.5)
print("| PRIZE!!!!!                     |         |    |   ")
time.sleep(0.5)
print("| So, what is the secret number? |         |   / \\")
time.sleep(0.5)
print("+================================+            /   \\")
time.sleep(0.5)

secret_number = 777                                             # declare secret number
guesses = 1                                                     # total guesses counter variable
guess_lst = []                                                  # empty list to catch all previous guesses
guess = int(input("\nEnter your guess: "))                      # number guess prompt

while guess != 777:                                             # while guess is not secret number enter loop
    print("Thinking......")                               # calculating guess
    time.sleep(0.5)                                             # add delay
    print(f"\nNot quite, you're stuck in my loop! You incorrectly guessed {guess}.")    # wrong guess
    guesses += 1                                                # increment guesses count by 1 after each guess
    guess_lst.append(guess)                                     # append last guess to guess list

    if "77" in str(guess):                                      # if "77" appears in guess at all, 2 numbers correct
        print("At least two of those digits is in my number, keep guessing!")
        guess = int(input("Enter your guess: "))

    elif "7" in str(guess):                                      # if "7" appears in guess at all, 1 number correct
        print("At least one of those digits is in my number, keep guessing!")
        guess = int(input("Enter your guess: "))

    elif guesses == 6:
        print("Ill give you a clue, the first digit begins with S")
        continue

    elif guesses == 10:
        print("I'll give you a second clue, the second digit begins with S!")
        continue

    else:
        guess = int(input("Enter your guess: "))

print("\nWell done, muggle! You are free now.")                             # correct guess
print(f"You guessed the secret number {guess} after {guesses} attempts.")   # fstring with correct guess & guess attempts
print(f"Your previous guesses were {guess_lst}")                            # fstring with all previous guesses

print("\nHere is your PRIZE!!!")                                              # reward correct guess with prize

for number in range(5):                                                     # short loop to create suspense
    dot = "."                                                               # define dot as "."
    dots = number * (dot *2)
    print(dots)
    time.sleep(1)

print("             *")                                                     # print wizard ascii image
time.sleep(0.25)
print("            / \\")
time.sleep(0.25)
print("           /___\\")
time.sleep(0.25)
print("           (o o)            * *")
time.sleep(0.25)
print("           ) L (           /  * *")
time.sleep(0.25)
print("  ________()(-)()________ /   * * *")
time.sleep(0.25)
print("E\\| _____ )()()()______ |/B    * * * *")
time.sleep(0.25)
print("| /       ()()()(      \\|      * * * * * *")
time.sleep(0.25)
print("          | )() |")
time.sleep(0.25)
print("         /       \\")
time.sleep(0.25)
print("        /  *   *  \\   A slightly less crapper wizard!")
time.sleep(0.25)
print("       /   *   *   \\")
time.sleep(0.25)
print("Credit: ascii.co.uk/art/wizard")                                 # image credit

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
