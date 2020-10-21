import pickle
import datetime
import os.path

FILENAME = 'insulin_data'

if not os.path.exists("./" + FILENAME):
	print ("Setting up...")
	ratios = []
	ratioBr = input("Ratio for Breakfast: ")
	while not ratioBr.isdigit():
		ratioBr = input("Ratio for Breakfast: ")
	ratios.append( int(ratioBr))
	ratioLu = input ("Ratio for Lunch: ")
	while not ratioLu.isdigit():
		ratioLu = input("Ratio for Lunch: ")
	ratios.append( int(ratioLu))
	ratioDi = input("Ratio for Dinner: ")
	while not ratioDi.isdigit():
		ratioDi = input("Ratio for Dinner: ")
	ratios.append (int(ratioDi))
	ratioBe = input("Ratio for night: ")
	while not ratioBe.isdigit():
		ratioBe = input("Ratio for night: ")
	ratios.append(int(ratioBe))
	outfile = open(FILENAME, 'wb')
	pickle.dump(ratios, outfile)
	outfile.close()
	


carbPrompt = "Enter carbs: "

carbs = input(carbPrompt)
while not carbs.isdigit():
	carbs = input(carbPrompt)
carbs = float(carbs)

ratioGet = input("Use ratio for: [B]reakfast, [L]unch, [D]inner or [N]ight? ")
ratioGet = ratioGet[0].lower()
infile = open(FILENAME, 'rb')
ratios = pickle.load(infile)
if ratioGet == "b":
	ratio = ratios[0]
elif ratioGet == "l":
	ratio = ratios[1]
elif ratioGet == "d":
	ratio = ratios[2]
elif ratioGet == "n":
	ratio = ratios[3]
else:
	ratioGet = input("Use ratio for: [B]reakfast, [L]unch, [D]inner or [N]ight? ")
	
	
insulin = carbs / ratio
insulin = float(insulin)
insulin = round(insulin * 2) / 2
print ("You need", insulin, "units")
