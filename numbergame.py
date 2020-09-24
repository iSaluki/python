import random
number = random.randint(1,100)
print (number)
attemptsLeft = 3
while attemptsLeft !=0:
	guess = input("What do you think the number is? ")
	while not guess.isdigit():
		guess = input("Not a number. Please enter a 	number.")
	guess = int(guess)
	if guess == number:
		print ("You win!")

	else:
		print ("Wrong!")
		if guess > number:
			guessIs = "too high"
		elif guess < number:
			guessIs = "too low"
		print (guess, "is", guessIs)
		attemptsLeft -= 1