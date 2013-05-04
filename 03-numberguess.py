# "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import math
import random
import simplegui

# initialize global variables used in your code
guesses = 0
secret = 0

# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global secret, guesses
    secret = random.randrange(0,100)
    guesses = 7
    print "New game. Range is from 0 to 100." #, secret
    print "Number of guesses remaining is", guesses
    print

def range1000():
    # button that changes range to range [0,1000) and restarts
    global secret, guesses
    secret = random.randrange(0,1000)
    guesses = 10
    print "New game. Range is from 0 to 1000.", secret
    print "Number of guesses remaining is", guesses
    print

def get_input(guess):
    # main game logic goes here
    global guesses
    guess = int(guess)
    
    print "Guess was", guess
    guesses -= 1
    print "Number of guesses remaining is", guesses
    if guesses >= 1:
        if guess == secret:
            print "Correct!"
            print
            range100()
        elif guess < secret:
            print "Higher!"
        elif guess > secret:
            print "Lower!"
        else:
            print "Try again..."
        
        print
    else:
        print "You ran out of guesses. The number was", secret
        print
        range100()

# create frame
f = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements
f.add_button("Range is [0, 100)", range100, 200)
f.add_button("Range is [0, 1000)", range1000, 200)
f.add_input("Enter a guess", get_input, 200)

# start frame
range100()
f.start()
