import math

while True:
	msg ="Enter number to square root: "

	num = input(msg)
	while not num.isdigit():
		num = input(msg)
	
	num = int(num)
	sqrt = (math.sqrt(num))
	print ("Square root:", sqrt)
