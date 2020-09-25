import math

msg_sqrt ="Enter number to square root: "
msg_init = "Choose function:"
msg_sqr = "Enter number to square:"

def Sqrt():		
	num = input(msg_sqrt)
	while not num.isdigit():
		num = input(msg_sqrt)
	
	num = float(num)
	sqrt = (math.sqrt(num))
	print ("Square root:", sqrt)
	
def Sqr():
	num = input(msg_sqr)
	while not num.isdigit():
		num = input(msg_sqr)
	sqr = float(num)**2
	print("Squared number:", sqr)

while True:
	print ("--------")
	print ("Functions:")
	print("[1] Square root")
	print ("[2] Square")
	function = input("Select function:")
	
	if function == "1":
		Sqrt()
	elif function == "2":
		Sqr()
	else:
		function = input("Select function:")
		
