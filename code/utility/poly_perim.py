class Shape:
	def __init__ (self,sides,length):
		self.sides = sides
		self.length = length
	def perimeter(self):
		return self.sides * self.length
		
		
inSides = input("Enter number of sides: ")
while not inSides.isdigit():
	inSides = input("Enter number of sides: ")
inSides = float(inSides)
inLength = input("Enter length of sides: ")
while not inLength.isdigit():
	inLength = input("Enter length of sides: ")
inLength = float(inLength)

polygon = Shape(inSides, inLength)


print ("The perimeter is", polygon.perimeter())
