# Lucky Unicorn Fully Working Program
# Program should work - needs to be tested for usability

import random

# Integer checking function
def intcheck(question, low, high):
    valid = False
    while not valid:

        error = "Whoops! Please enter an integer between {} and ${}".format(low, high)

        try:
            response = int(input("How much do you want to play with? (between ${:.2f} and ${:.2f}): ".format(low, high)))

            if low <= response <= high:
                return response
            else:
                print(error)
                print()
        except ValueError:
            print(error)

# Main routine

# Ask user how much they want to play with (min $1, max $10)
print("welcome to the lucky unicorn game")
print()
print("To play, enter an amount of money between $1 and $10 (whole dollars only).")
print()
print("- It costs $1/round")
print()
print("Payouts...")
print("- Unicorn: $5.00")
print("- Horse / Zebra: $0.50")
print("- Donkey: $0.00")
print()
balance = intcheck("How much money would you like to play with? ", 1, 10)

keep_going = ""
while keep_going == "":

    # tokens list includes 10 items to prevent too many unicorns being chosen
    tokens = ["horse","horse","horse",
              "zebra","zebra","zebra",
              "donkey","donkey","donkey","unicorn"]

    # Randomly choose a token from our list above
    token = random.choice(tokens)
    print()
    print("You got a {}".format(token))

    # Adjust total correctly for a given token
    if token == "unicorn":
        balance += 4    # wins $5 (1 dollar payment)
        feedback = "Oh no, you won $5.00"
    elif token == "donkey":
        balance -= 1    # loses $1
        feedback = "Congratulations, you lost $1"
    else:
        balance -= 0.5  # loses 50c
        feedback = "Congratulations, you lost 50c"

    print()

    print(feedback)
    print("You have ${:.2f} left to give us".format(balance))
    print()

    # If user has enough money to play, ask if they want to play again...
    if balance < 1:
        print("Sorry you don't have enough money to continue.  GAME OVER")
        keep_going = "end"
    else:
        keep_going = input("Press <enter> to play again or any key to quit")

# farewell user at end of game.
print("Thank you for playing")






