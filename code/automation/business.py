
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
		

print ("Business Studies Calculator - Developed by Seth-Maurice Brant under MIT license. Source code access and modification allowed.")
print ("")
currencyCode = input("Enter currency symbol: ")

while True:
		print ("")
		print ("Function List:")
		print ("[P] Profit calculator")
		print ("[B] Break Even Point calculator")
		funcSelector =  input("Please select function: ")
		funcSelector = funcSelector[0].lower()
		if funcSelector == "p":
			print ("Starting profit calculator.")
			CalcProfit()
		elif funcSelector == "b":
			print ("Startig break even point calculator.")
			BreakEven()
		else:
			print ("Unknown function")
	
	
