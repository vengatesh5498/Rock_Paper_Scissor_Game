from random import choice

while True:
    choices=["rock","paper","scissors"]

    computer= choice(choices)
    player=None

    while player not in choices:
        player=input("rock, paper, scissors?: ").lower()
    if player==computer:
            print("computer: ",computer)
            print("player: ",player)
            print("It's a Tie!")
    elif player=="rock":
        if computer=="paper":
            print("computer: ",computer)
            print("player: ",player)
            print("You Lose !")
        if computer=="scissors":
            print("computer: ",computer)
            print("player: ",player)
            print("You Win !")
    elif player=="paper":
        if computer=="scissors":
            print("computer: ",computer)
            print("player: ",player)
            print("You Lose !")
        if computer=="rock":
            print("computer: ",computer)
            print("player: ",player)
            print("You Win !")
    elif player=="scissors":
        if computer=="paper":
            print("computer: ",computer)
            print("player: ",player)
            print("You Win !")
        if computer=="rock":
            print("computer: ",computer)
            print("player: ",player)
            print("You Lose !")

    play_again=input("Play again? (Yes/No):").lower()
    if play_again != "yes":
        break
print("Bye!")