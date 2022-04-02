import random

wordList = ['HOUSE', 'APPLE', 'PIZZA', 'ROUND', 'GREEN']
word = random.choice(wordList)
guess = '*****'

import turtle

turtle.pensize(5)
errors = 0


def showHangman():
    if (errors == 1):
        turtle.bk(100)
        turtle.fd(200)
    if (errors == 2):
        turtle.bk(100)
        turtle.lt(90)
        turtle.fd(300)
    if (errors == 3):
        turtle.rt(90)
        turtle.fd(150)
    if (errors == 4):
        turtle.rt(90)
        turtle.fd(50)
    if (errors == 5):
        turtle.dot(50)
    if (errors == 6):
        turtle.fd(100)
        turtle.bk(75)
    if (errors == 7):
        turtle.rt(45)
        turtle.fd(50)
        turtle.bk(50)
    if (errors == 8):
        turtle.lt(90)
        turtle.fd(50)
        turtle.bk(50)
    if (errors == 9):
        turtle.rt(45)
        turtle.fd(75)
        turtle.rt(45)
        turtle.fd(50)
        turtle.bk(50)
    if (errors == 10):
        turtle.lt(90)
        turtle.fd(50)


while ((guess != word) and (errors < 10)):
    print('Here is the word ', guess)
    letter = input('Guess a letter ')
    letter = letter.upper()
    hasLetter = False
    newguess = []

    for n in range(5):
        if (letter == word[n]):
            newguess.append(letter)
            hasLetter = True
        else:
            newguess.append(guess[n])
    guess = ''.join(newguess)

    if (hasLetter == True):
        print('Good guess')
    else:
        print('Not in the word')
        errors = errors + 1
        showHangman()

print('The word was', word)
'''
hangman
graphical.py
Displaying
hangman
graphical.py.
Code Max Wainewright
'''

