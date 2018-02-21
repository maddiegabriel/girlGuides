#!/usr/bin/python
import time
import random
import colorama
from colorama import Fore, Style, Back #BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE

#variables:

className = 'history'
numOfDoodles = 0
appleInYourLunch = 'yes'
numOfGoals = 5
sport = 'basketball'
posAdjective = 'cool'
numOfQuestions = 3
colour = 'red'
weekday = 'Monday'








#story:

print(Style.RESET_ALL)
#print(Fore.BLUE)
#print(Back.GREEN)

print ("\nToday is " + weekday + " morning, and you are sitting in class for a "+ className +" lesson.")
print("Your teacher is talking about something really boring.")

input() #pause








#print(Fore.GREEN)
print("So you decided to draw " + str(numOfDoodles) + " doodles on a page in your " + colour + " notebook.")
print("You wonder when " + className + " class will end.")

print("Before you know it, it is lunchtime. You've noticed that one of your friends has goldfish crackers.")
print("You rather eat that than your lunch.")

input() #pause









print("She said that if you have an apple, you can trade with her for crackers.")

#if and else block
if appleInYourLunch == 'yes':
	print("Fortunately, you do have an apple in your bag! You enjoyed your lunch today.")
elif appleInYourLunch == 'no':
	print("Today is not your lucky day. You eat your lunch without joy.")

input() #pause









print("Now it's gym class! You are amazing in " + sport + " because it is your favourite sport.")

print("So you scored a goal...")

for x in range(0, numOfGoals): #loop
    print ("And another...")
    time.sleep(1) 

print("You're a " + posAdjective + " superstar in this gym class!")
input() #pause








print("Before you know it, it's the last class of the day.")
print("You love math class so much, that you don't mind a pop quiz.")
print("And a pop quiz is what you got today!")
input() #pause










print("You read the questions in front of you.")
for x in range(0, numOfQuestions): #loop

	print("\nIn question " + str(x + 1) + ",")
	firstNum = int(random.randint(1,10)) #get the first number
	secondNum = int(random.randint(1,12)) #get the second number
	print("What's " + str(firstNum) + " plus " + str(secondNum) + "?")

	playersAnswer = input() #your answer to the question
	total = firstNum + secondNum

	if(int(playersAnswer) == total): #you got the answer right!
		print("You got it right!")
	else: #nope!
		print("Oh no! You didn't get this one right.")








print("\nYou have reached the end of the school day, and although you enjoyed it, you can't help but wonder...")
print("... Could things have been different?")
input() #pause

print(Style.RESET_ALL)








