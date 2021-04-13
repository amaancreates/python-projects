import random

def play():
    user = input("What's your choice? 'R' for rock, 'P' for paper, 'S' for scissor \n")
    computer = random.choice(["R", 'P', 'S'])

    if user == computer:
        return 'It\'s a tie'
    
    if is_win(user, computer):
        return 'You won!'
    return "You lost"

def is_win(player, opponent):
    if (player == "R" and opponent == "P") or (player == "P" and opponent == "S") or (player == "S" and opponent == "P"):
        return True

print(play())
     
input()
    
