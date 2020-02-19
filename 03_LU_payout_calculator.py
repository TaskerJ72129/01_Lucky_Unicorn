# Lucky Unicorn Decomposition Step 3
# Generate a random token

import random

HOW_MUCH = 100
tokens = ["horse", "zebra", "donkey", "unicorn"]

unicorn_count = 0
zebhorse_count = 0
donkey_count = 0

for item in range(0,HOW_MUCH):

    chosen = random.choice(tokens)

    if chosen == "unicorn":
        unicorn_count += 1
    elif chosen == "donkey":
        donkey_count += 1
    else:
        zebhorse_count += 1

    print(chosen)

# Money Calculations
winnings = unicorn_count * 5 + zebhorse_count * 0.5

print("**** Win / Loss Calculations ****")
print("# Unicorns: {}".format(unicorn_count))
print("# Zebra / Horses: {}".format(zebhorse_count))
print("# Donkeys: {}".format(donkey_count))

print()
print("You spent ${}".format(HOW_MUCH))
print("You go home with ${}".format(winnings))