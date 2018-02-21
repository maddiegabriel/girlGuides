#!/usr/bin/python
import time
import random

#variables

playersChoice = ''
computerChoice = ''
numOfRounds = 0
computerScore = 0
playerScore = 0
choices = ['paper', 'scissors', 'rock']

#game:
print("\nWelcome! You are playing 'rock paper scissors' with the computer!")
print("How many rounds of 'rock paper scissors' do you want to play?")
numOfRounds = input()
numOfRounds = int(numOfRounds) #make it into a number

for x in range(0, numOfRounds):
	computerChoice = random.choice(choices)#computer make a choice

	print("\nRound " + str(x + 1))
	print("You choose...")
	playersChoice = input() #you make a choice
	print("The computer chose " + computerChoice)

	if (computerChoice == 'rock' and playersChoice == 'paper'):
		print("You win!")
		playerScore += 1

	elif (computerChoice == 'rock' and playersChoice == 'scissors'):
		print("The computer win!")
		computerScore += 1

	elif (computerChoice == 'paper' and playersChoice == 'rock'):
		print("The computer wins!")
		computerScore += 1

	elif (computerChoice == 'paper' and playersChoice == 'scissors'):
		print("You win!")
		playerScore += 1

	elif (computerChoice == 'scissors' and playersChoice == 'paper'):
		print("The computer wins!")
		computerScore += 1

	elif (computerChoice == 'scissors' and playersChoice == 'rock'):
		print("You win!")
		playerScore += 1

	elif (computerChoice == playersChoice): 
		print("It's a tie!")

print("\nScore:")
print("Computer: " + str(computerScore))
print("You: " + str(playerScore))

