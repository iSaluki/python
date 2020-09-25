import random
number = random.randint(1,100)
# print (number) 
# Enable the above line by removing the '#'. It will print the random number for debug purposes.
totalAttempts = 0
hasWon = False
highscores = []
newGame = "y"

def Win():
	global totalAttempts, newGame
	print ("It took you", totalAttempts, "guesses to get the number")
	name = input("What is your name? ")
	highscores.append([name, totalAttempts])
	print (highscores)
	totalAttempts = 0
	newGame = input("Would you like to play again?[y/n] ")
	newGame = newGame[0].lower()


while  newGame == "y":
	guess = input("What do you think the number is? ")
	while not guess.isdigit():
		guess = input("Not a number. Please enter a 	number.")
	guess = int(guess)
	if guess == number:
		print ("You win!")
		hasWon == True
		newGame == "n"
		number = random.randint(1,100)
		Win()
	else:
		print ("Wrong!")
		if guess > number:
			guessIs = "too high"
		elif guess < number:
			guessIs = "too low"
		print (guess, "is", guessIs)
		totalAttempts += 1
#if newGame != "y":
print ("Goodbye!")
