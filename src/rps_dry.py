import random
# create a simple rock paper scisors game in python

# Create a rock/paper/scissors REPL
# Have a computer AI to play agains us
# keep track of a score
# RULES: r beats s, s beats p, p beats r

# set up some sentinal values for variables
wins = 0
losses = 0
ties = 0
# set up a list of possible choices
choices = ["r", "p", "s"]

# a function that compares choices

    #test if player_choice is equal to computer_choice
        # return 0
    # otherwise (if pc is r and cc is s) 
    # or (pc is p and cc is r) or
    # (pc s and cc is p)
        # return 1
    # otherwise
        # return -1

# start a REPL
while True:
    # show score
    print(f"Score: {wins} - {losses} - {ties}")
    # take input from the player
    cmd = input("\nChoose r/p/s/q: ")
    # have the AI make a random choice of r/p/s
    ai_choice = choices[random.randrange(3)]
    # show the AI choice
    print(f"Computer Chose {ai_choice}")
    # conditional logic or commande
    
    else:
        print("I do not understand that command")
        
        
