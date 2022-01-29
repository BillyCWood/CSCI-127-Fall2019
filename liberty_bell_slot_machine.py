# ---------------------------------------
# CSCI 127, Joy and Beauty of Data
# Program 1: Liberty Bell Slot Machine
# ---------------------------------------
# Simulate a modified Liberty Bell Slot Machine.
# ---------------------------------------

import random

# Constants that represent the result of spinning a reel
DIAMOND = 1     
HEART = 2
SPADE = 3
HORSESHOE = 4
LIBERTY_BELL = 5

# ---------------------------------------
# spin_payout
# ---------------------------------------
# reel_1: the symbol on the first reel, an integer constant
# reel_2: the symbol on the second reel, an integer constant
# reel_3: the symbol on the third reel, an integer constant
# ---------------------------------------
# Returns an integer, the payout of the spin
# ---------------------------------------

""" The missing spin_payout function goes here ... """

def spin_payout(reel_1, reel_2, reel_3):
    if reel_1 == LIBERTY_BELL and reel_2 == LIBERTY_BELL and reel_3 == LIBERTY_BELL:
        return 50
    elif reel_1 == HEART and reel_2 == HEART and reel_3 == HEART:
        return 40
    elif reel_1 == DIAMOND and reel_2 == DIAMOND and reel_3 == DIAMOND:
        return 30
    elif reel_1 == SPADE and reel_2 == SPADE and reel_3 == SPADE:
        return 20
    elif reel_1 == HORSESHOE and reel_2 == HORSESHOE and reel_3 == HORSESHOE:
        return 10
    elif (reel_1 == HORSESHOE and reel_2 == HORSESHOE) or (reel_1 == HORSESHOE and reel_3 == HORSESHOE) or (reel_2 == HORSESHOE and reel_3 == HORSESHOE):
        return 5
    else:
        return 0

# ---------------------------------------
# convert
# ---------------------------------------
# reel: the symbol on a reel, an integer constant
# ---------------------------------------
# Returns a string, the printing value of integer
# ---------------------------------------

def convert(reel):
    if reel == DIAMOND:
        return "diamond"
    elif reel == HEART:
        return "heart"
    elif reel == SPADE:
        return "spade"
    elif reel == HORSESHOE:
        return "horseshoe"
    elif reel == LIBERTY_BELL:
        return "bell"
    else:
        return "error!"

# ---------------------------------------
# test_known_spin
# ---------------------------------------
# reel_1: the symbol on the first reel, an integer constant
# reel_2: the symbol on the second reel, an integer constant
# reel_3: the symbol on the third reel, an integer constant
# ---------------------------------------
# Display a message that shows the spin and its payout
# ---------------------------------------

def test_known_spin(reel_1, reel_2, reel_3):
    message = "{:10}".format(convert(reel_1))
    message += "{:10}".format(convert(reel_2))
    message += "{:10}".format(convert(reel_3))
    message += "{:-6d}".format(spin_payout(reel_1, reel_2, reel_3))
    print(message)

# ---------------------------------------
# test_known_spins
# ---------------------------------------
# For testing purposes, evaluate a variety of known spins
# ---------------------------------------

def test_known_spins():
    print("{:10}{:10}{:10}{}".format("REEL 1", "REEL 2", "REEL 3", "PAYOUT"))
    print("{:10}{:10}{:10}{}".format("------", "------", "------", "------"))
    test_known_spin(LIBERTY_BELL, LIBERTY_BELL, LIBERTY_BELL)
    test_known_spin(HEART, HEART, HEART)
    test_known_spin(DIAMOND, DIAMOND, DIAMOND)
    test_known_spin(SPADE, SPADE, SPADE)
    test_known_spin(HORSESHOE, HORSESHOE, HORSESHOE)
    test_known_spin(HORSESHOE, HORSESHOE, HEART)
    test_known_spin(HORSESHOE, DIAMOND, HORSESHOE)
    test_known_spin(SPADE, HORSESHOE, HORSESHOE)
    test_known_spin(HEART, HEART, HORSESHOE)
    test_known_spin(LIBERTY_BELL, DIAMOND, SPADE)

# ---------------------------------------
# simulate
# ---------------------------------------
# how_many: the number of spins to take, an integer
# ---------------------------------------
# Simulate the Liberty Bell Slot Machine being played
# how_many times.  Calculate and print the expected winnings.
# ---------------------------------------

""" The missing simulate function goes here ... """

def simulate(how_many):
    winnings = 0

    for i in range(how_many):
        reel_1 = random.randint(1,5)
        reel_2 = random.randint(1,5)
        reel_3 = random.randint(1,5)
        
        winnings += (spin_payout(reel_1, reel_2, reel_3)/100)


    return winnings/25000 #25,000 is the amount of nickels in 500,000 cents

# ---------------------------------------
# main - controls the main flow of logic
# ---------------------------------------

def main():
    print("Program 1: Liberty Bell Slot Machine Simulation\n")
    print("--> Part 1: Testing Known Spins\n")
    test_known_spins()
    print("\n--> Part 2: Simulating 500,000 Spins\n")
    probability = simulate(500000)
    print("For every $1 spent, you can expect to win {:.2f}".format(probability))
          
# ---------------------------------------

main()
