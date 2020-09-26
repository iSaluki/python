class Shape:
	def __init__ (self,sides,length):
		self.sides = sides
		self.length = length
inSides = input("Enter number of sides: ")
while not inSides.isdigit():
	inSides = input("Enter number of sides: ")
inSides = float(inSides)
inLength = input("Enter length of sides: ")
while not inLength.isdigit():
	inLength = input("Enter length of sides: ")
inLength = float(inLength)

Shape.sides = inSides
Shape.length = inLength

output = Shape.length * Shape.sides
print ("The perimeter is", output)
