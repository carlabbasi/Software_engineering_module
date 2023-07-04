# Wed5July.py

# 3.2.1.9 LAB - Random word guesser
print("*** While loop secret word guesser ***")

print("\nGuess the secret word to exit the loop!")
user = input("What is your guess? ")
user = user.upper()

while True:                                                  # enter while loop
    if user == "CHUPACABRA":                                 # if / break clause
        print("Correct!!")
        break
    user = input("Incorrect, try again: ")                   # user input
    user = user.upper()

print("You've successfully left the loop")                   # loop exit statement
print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")


# 3.2.1.10 LAB - The ugly vowel eater
print("\n*** The ugly vowel eater! ***")

word = input("Enter a word to put in the vowel eater: ")    # user prompt
word = word.upper()                                         # convert string to upper case

for letter in word:                                         # enter for loop
    if letter == "A":                                       # check if letter is = A
        continue
    elif letter == "E":                                     # check if letter is = E
        continue
    elif letter == "I":                                     # check if letter is = I
        continue
    elif letter == "O":                                     # check if letter is = O
        continue
    elif letter == "U":                                     # check if letter is = U
        continue
    else:
        print(letter)                                       # if letter != vowel, print letter to console
print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")


# 3.2.1.11 LAB - The pretty vowel eater
print("\n*** The pretty vowel eater! ***")

word = input("Enter a word to put in the vowel eater: ")    # user prompt
word = word.upper()                                         # convert string to upper case
new_word = ""                                               # empty variable for non vowel letter

for letter in word:                                         # enter for loop
    if letter == "A":                                       # check if letter is = A
        continue
    elif letter == "E":                                     # check if letter is = E
        continue
    elif letter == "I":                                     # check if letter is = I
        continue
    elif letter == "O":                                     # check if letter is = O
        continue
    elif letter == "U":                                     # check if letter is = U
        continue
    else:
        new_word += letter                                  # if letter != vowel add to new_word variable

print(new_word)                                             # when loop exits, print variable new_word
print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
