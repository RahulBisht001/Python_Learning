# Simple Guess Game
import random

randomNumber = random.randint(1, 50)
# gameResult = 0
primeList = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

print("Make a Guess for a Random Number based on the hints")
print("You have only Three Chances")

# Using Ternary Operator
print("Hint 1: ")
firstHint = 'Number is Even' if randomNumber % 2 == 0 else print('Number is Odd')
print(firstHint)


print('Now guess the Number')
guessCount = 1

"""
Using while loop
in python while loop also have a else condition
that can be executed only if while loop run successfully 
without any break Statement.
"""

while guessCount != 4:
    if guessCount == 2:
        if randomNumber < 25:
            print('Number is less than 25')
        else:
            print('Number is Greater than or Equal to 25')

    if guessCount == 3:
        if randomNumber in primeList:
            print('Number is a Prime Number')
        else:
            print('Number is not a Prime Number')

    a = int(input('Number May Be: '))
    if a == randomNumber:
        print('BooYeah You Guess it correct')
        gameResult = 1
        break
    guessCount += 1

else:
    print('You Lose the Game Buddy')
    print('Correct Ans was  ' + str(randomNumber))
