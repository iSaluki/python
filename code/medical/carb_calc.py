weight = input("Total weight: ")
while not weight.isdigit():
	weight = input("Total weight: ")
weight = float(weight)
carbs = input("Carbs per 100g: ")
while not carbs.isdigit():
	carbs = input("Carbs per 100g: ")
carbs = float(carbs)

pw = carbs / 100 
totalCarbs = pw * weight
print ("Total carbs is ", totalCarbs, "g")

