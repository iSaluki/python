
def CalcProfit():
			revenue = input("Enter revenue: ")
			while not revenue.isdigit():
				revenue = input("Enter revenue: ") 
			costs = input("Enter costs: ")
			while not costs.isdigit():
			 	costs = input("Enter costs: ")
			costs = float(costs)
			revenue = float(revenue)
			print (currencyCode,revenue - costs, "profit")
	
def BreakEven():
			costs = input("Enter fixed costs: ")
			while not costs.isdigit():
				costs = input("Enter fixed costs: ")
			sellPrice = input("Enter selling price per unit: ")
			while not sellPrice.isdigit():
				sellPrice = input("Enter selling price per unit: ")
			varCosts = input("Enter variable cost per unit: ")
			while not varCosts.isdigit():
				varCosts = input("Enter variable cost per unit: ")
			costs = float(costs)
			sellPrice = float(sellPrice)
			varCosts = float(varCosts)
			bep = costs / (sellPrice - varCosts)
			bep = int(bep)
			print ("Break even at", bep, "sales")
def MOS():
		bep = input("Enter break even point: ")
		while not bep.isdigit():
			bep = input("Enter break even point: ")
		sales = input("Enter sales: ")
		while not sales.isdigit():
			sales = input("Enter sales: ")
		sales = int(sales)
		bep = int(bep)
		print ("Your margin of safey is", sales-bep, "sales")
		

print ("Business Studies Calculator - Developed by Seth-Maurice Brant under MIT license. Source code access and modification allowed.")
print ("")
currencyCode = input("Enter currency symbol: ")

while True:
		print ("")
		print ("Function List:")
		print ("[P] Profit calculator")
		print ("[B] Break Even Point calculator")
		print ("[M] Margin of Safety calculator")
		funcSelector =  input("Please select function: ")
		funcSelector = funcSelector[0].lower()
		if funcSelector == "p":
			print ("Starting profit calculator.")
			CalcProfit()
		elif funcSelector == "b":
			print ("Starting break even point calculator.")
			BreakEven()
		elif funcSelector == "m":
			print ("Starting Margin of Safety calculator")
			MOS()
		else:
			print ("Unknown function")
	
	
