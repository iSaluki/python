import random

print ("Welcome to the game!")
newGame = "y"
while newGame == "y":
	attemptsLeft = 3
	while attemptsLeft >0:
		attempt = input("What is the secret word? ")
		words = ["apple","orange","pear", "balloon",      "orchid"]
		secret = words[random.randint(0,4)]
		if attempt == secret:
			print ("You win!")
			attemptsLeft = 0
		else:
			print ("Nope! Have another go.")
			attemptsLeft -= 1
	print ("Game Over!")
	newGame = input("Would you like to start a new game? [y/n] ")
	newGame = newGame[0].lower()