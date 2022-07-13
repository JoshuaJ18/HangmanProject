#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      joshu
#
# Created:     25/02/2021
# Copyright:   (c) joshu 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#Intro Function
def intro():
    print ("Hangman")
    print ("")
    print ("In order to win in this Hangman game you must accurately guess the word before the hangman is fully drawn.")
    print ("You may choose the letters in the word individually or you can try to guess the full word.")
    print ("If the chosen letter or word is incorrect then one piece of the hangman will be drawn.")
    print ("You will have to complete 5 words in order to win the game, and if a hangman is drawn then you must start the game over.")
    print ("To start the game, type 'enter'")
#Hangman Words
green = ["g", "r", "e", "e", "n"]
correctgreen = []

#Win/Loss Variable
L = 0

#Image

ima = (0)
def image():
    if ima == 0:
        print ("")
        print ("")
        print ("")
        print ("")
        print ("")
        print ("Correct letters: ")
        print (correctgreen)
    elif ima == 1:
        print (" O")
        print ("")
        print ("")
        print ("")
        print ("")
        print ("Correct letters: ")
        print (correctgreen)
    elif ima == 2:
        print (" O")
        print (" \ /")
        print ("")
        print ("")
        print ("")
        print ("Correct letters: ")
        print (correctgreen)
    elif ima == 3:
        print (" O")
        print (" \ /")
        print (" |")
        print ("")
        print ("")
        print ("Correct letters: ")
        print (correctgreen)
    elif ima == 4:
        print (" O")
        print (" \ /")
        print (" |")
        print (" |")
        print ("")
        print ("Correct letters: ")
        print (correctgreen)
    elif ima == 5:
        print (" O")
        print (" \ /")
        print (" |")
        print (" |")
        print (" / \ ")
        print ("Correct letters: ")
        print (correctgreen)

#Win Scenario
def win():
    image()
    print("Congratulations!")
    print("You have won the game!")

#First round
def first():
#This method (global ima) came from this website: https://stackoverflow.com/questions/18002794/local-variable-referenced-before-assignment
    global ima
    word = input("Enter a letter: ")

    if len(green) > 1:
        if word in green:
            if word == "g":
                correctgreen.append("g")
                green.remove("g")
                image()
                if ima < 5:
                    first()

            elif word == "r":
                correctgreen.append("r")
                green.remove("r")
                image()
                if ima < 5:
                    first()
            elif word == "e":
                correctgreen.append("e")
                green.remove("e")
                correctgreen.append("e")
                green.remove("e")
                image()
                if ima < 5:
                    first()
            elif word == "n":
                correctgreen.append("n")
                green.remove("n")
                image()
                if ima < 5:
                    first()
        elif word == "green":
            correctgreen.append("g")
            green.remove("g")
            correctgreen.append("r")
            green.remove("r")
            correctgreen.append("e")
            green.remove("e")
            correctgreen.append("e")
            green.remove("e")
            correctgreen.append("n")
            green.remove("n")
            win()

        else:
            print ("Wrong! That letter was not in the word, guess again!")
            ima = 1 + ima
            image()
            if ima < 5:
                first()
    else:
        correctgreen.append("n")
        win()

#Hangman Image
intro()
gamestart = input("")

#gamestart
if gamestart == "enter":
    print ("First Round:")
    first()
else:
    print ("")
    intro()



