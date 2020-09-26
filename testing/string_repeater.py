string = input("String:")
stringSuffix = " "
string = string + stringSuffix
times = input("Amount:")
while not times.isdigit():
	times= input("Amount")
times = int(times)
print (string * times)
