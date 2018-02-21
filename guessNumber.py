#!/usr/bin/python
import time
import random

#variables

playersChoice = ''
computerChoice = ''
numOfRounds = 0
computerScore = 0
playerScore = 0

#game:
print("\nIn this game, you have to guess what number the computer chose. If you are right, you win a point!")
print("How many times you want to guess the number?")
numOfRounds = input()
numOfRounds = int(numOfRounds) #make it into a number

for x in range(0, numOfRounds):
	computerChoice = int(random.randint(1,5))#computer make a choice

	print("\nRound " + str(x + 1))
	print("You choose...")
	playersChoice = int(input()) #you make a choice
	print("The computer chose " + str(computerChoice))

	if (computerChoice < playersChoice):
		print("You lost, your number was too high!")
		
	elif (playersChoice < computerChoice):
		print("You lost, your number was too low!")

	elif (computerChoice == playersChoice): 
		print("It's a tie! You guessed the number right!")
		playerScore += 1

print("\nScore:")
print("You: " + str(playerScore))

