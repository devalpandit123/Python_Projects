# *******************Project 1: Color Choice Game******************************

# Project Helpful Notes:
# 1.We need to create choices for players and choices for computer then ask the players for inputs.
# 2.Compare their inputs with the choice of the computer.
# 3.Check if the game is won, tied, lost, or ongoing.
# 4.Repeat thess steps until the game has been won or tied.
# 5.Ask if players want to play again.
# 6.If the players agree restart the game again.
# 7.If the player say "No" end the game and say thanks for the player.

# *****************************************************************************

import random
print("Winning Rules of the Colors choices Game as follows: " +
      "\nEnter a number from one two five and match computer choice to Win the computer.")
print("red = 1 \nyellow = 2 \norange = 3 \ngreen = 4 \nblue = 5 \ntake a turn: ")
user, computer, counter = 0, 0, 0
playButton = input("Do you want to play?(Y/N) ")
while(True):
    if(playButton == 'Y' or playButton == 'y'):
        numColorDict = {1: "red", 2: "yellow",
                        3: "orange", 4: "green", 5: "blue"}
        while counter != 1:
            userSelection = input(
                "Select a number between 1 and 5, press N/n to end the game: ")
            print("-----------{}".format(numColorDict.keys()))
            try:
                if int(userSelection) in numColorDict.keys():
                    print("Your selected color : {}. Let us see what computer selects the color".format(
                        numColorDict.get(int(userSelection))))
                    computerSelection = random.randint(1, 5)
                    print("Computer selected : {}".format(
                        numColorDict.get(int(computerSelection))))
                    if int(userSelection) == computerSelection:
                        user += 1
                    else:
                        computer += 1
                    print("User points : ", user)
                    print("Computer points : ", computer)
                else:
                    print("Invalid input, please try again!")
                break
            except ValueError:
                if userSelection == 'N' or userSelection == 'n':
                    print("Thank you for playing the game.")
                    if user > computer:
                        print("The winner of the match is USER")
                    elif computer > user:
                        print("The winner of the match is COMPUTER")
                    elif computer == 0 and user == 0:
                        print("Match not started. Start the game again.")
                    elif computer == user:
                        print("Match is tied")
                    else:
                        print("Wrong input. Please start the game again")
                    counter = 1
                    break
                else:
                    print("Wrong selection, please try either n or N")
    elif(playButton == 'N' or playButton == 'n'):
        print("Thank you for playing the game.")
        if user > computer:
            print("The winner of the match is USER")
        elif computer > user:
            print("The winner of the match is COMPUTER")
        elif computer == 0 and user == 0:
            print("Match not started. Start the game again.")
        elif computer == user:
            print("Match is tied")
        else:
            print("Wrong input. Please start the game again")
        break
    else:
        print("Wrong input, Please try again!")
        playButton = input("Do you want to play?(Y/N) ")
