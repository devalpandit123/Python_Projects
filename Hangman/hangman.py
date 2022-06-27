from hangman_life_details import lives, game_name
from hangman_fruit_list import guess_list
import random

variableForUser = ""
counter = 0
counterLetter = 6
randomChoiceByComputer = random.choice(guess_list)
print("Welcome to HangMan!!")
print("Guess the word. Your get 6 tries to identify the word. Let's atart the game!!")
#print(randomChoiceByComputer)
while(True):    
    takeInputLetter = input("Guess the letter: ")
    if counter == 0:
        for lengthVar in randomChoiceByComputer:
            variableForUser+="_"
    listVar = list(variableForUser)
    #print("variableForUser=",listVar)
    for j, letter in enumerate(randomChoiceByComputer):
        if letter == takeInputLetter:
            print("---Found---")
            listVar[j] = takeInputLetter
            variableForUser = "".join(listVar)
        elif letter.swapcase() == takeInputLetter:
            print("---Found Here---")
            listVar[j] = takeInputLetter.swapcase()
            variableForUser = "".join(listVar)
    if(takeInputLetter not in randomChoiceByComputer and takeInputLetter.swapcase() not in randomChoiceByComputer):
        #print("----CounterLetter----", counterLetter)
        if counterLetter == 0:
            print(lives[counterLetter])
            print("You have no more tries left")
            print("You have failed")
            print("The item is {}".format(randomChoiceByComputer))
            break
        print(lives[counterLetter])
        print("You have {} more tries left".format(counterLetter))
        counterLetter -= 1
    if(variableForUser == randomChoiceByComputer):
        print(variableForUser)
        print(game_name)
        print("Congratulations!!!! You found the solution")
        break
    print(variableForUser)
    counter += 1