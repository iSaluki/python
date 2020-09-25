carbPrompt = "Enter carbs: "
ratioPrompt = "Enter ratio: "

carbs = input(carbPrompt)
while not carbs.isdigit():
	carbs = input(carbPrompt)
carbs = float(carbs)
	
ratio = input(ratioPrompt)
while not ratio.isdigit():
	ratio = input(ratioPrompt)
ratio = float(ratio)

insulin = carbs / ratio
insulin = float(insulin)
print ("You need", insulin, "units")
