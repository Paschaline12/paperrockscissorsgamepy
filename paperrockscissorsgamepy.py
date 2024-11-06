import random

options = ("rock", "paper", "scissors")
player = None
computer = random.choice(options)

while player not in options:
    player = input("Enter a choice between rock, paper and scissors: ")

print(f"player: {player}")
print(f"computer: {computer}")

if player == computer:
    print("Congratulations, it is a tie")
elif player == "rock" and computer =="scissors":
    print("You win.... This is a hit")
elif player == "paper" and computer == "rock":
    print("You came close to a tie, please play again")
elif player == "scissors" and computer == "paper":
    print("One more trial for you to win: Please play again")
else:
    print("Please take a break")
    