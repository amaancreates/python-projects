import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    guess = random.randint(low, high)
    
    #starting of infinite loop in below lines
    valid = False
    while not valid:
        feedback = (input(f"Is {guess} too high(H), too low(L), OR CORRECT(C)?"))
        if feedback == "H":
            guess = guess - 1
            
        elif feedback == "L":
            guess = guess + 1
            
        elif feedback == "C":
            print(f"Yay! The computer guessed your number, {guess}, correctly!")
            
        else:
            print("invalid input")
            
        
    

computer_guess(10)

input()

