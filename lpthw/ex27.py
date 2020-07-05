# BRANCHES AND FUNCTIONS

from sys import exit
# To import exit function
def gold_room():
    print("This room is full of gold. How much do you take?")
    choice = input(">>> ")
    # To check if the input is a number but the method is very
    # inefficient, it'll only check for 0's and 1's
    if "0" in choice or "1" in choice:
        how_much = int(choice)
# Convert a number or string to an integer, or return 0 if no arguments
# are given.  If x is a number, return x.__int__().  For floating point
# numbers, this truncates towards zero.
# If x is not a number or if base is given, then x must be a string,
# bytes, or bytearray instance representing an integer literal in the
# given base.  The literal can be preceded by '+' or '-' and be surrounded
# by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
# Base 0 means to interpret the base from the string as an integer literal.
# >>> int('0b100', base=0)
# 4
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard.")

def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        choice = input(">>> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")

def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = input(">>> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty. Wasn't it?")
    else:
        cthulhu_room()

def start():
    print("You're in a dark room.")
    print("There is a door to your left and right.")
    print("Which one do you take?")

    choice = input(">>> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

def dead(why):
    print(why, "Good job!")
    exit(0)

start()
