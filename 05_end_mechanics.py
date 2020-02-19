# Lucky Unicorn - end mechanics

# Assusme starting amount is $10
total = int(input("How much do you want to play with? "))

keep_going = ""
while keep_going == "":

    # Allow manual token input for testing purposes
    token = input("enter a token: ")

    # Adjust total correctly for a given token
    if token == "unicorn":
        total += 5
        feedback = "Oh no, you won $5.00"
    elif token == "donkey":
        total -= 1
        feedback = "Congratulations, you won nothing"
    else:
        total -= 0.5
        feedback = "Congratulations, you lost 50c"

    print()

    print(feedback)
    print("You have ${:.2f} left to give us".format(total))

    if total < 1:
        print("Sorry you don't have enough money to continue.  GAME OVER")
        keep_going = "end"
    else:
        keep_going = input("Press <enter> to play again or any key to quit")

print("Thank you for playing")