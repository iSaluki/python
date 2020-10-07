number = input("Enter number: ")
while not number.isdigit():
  number = input("Enter number: ")
number = int(number)
hexOutput = hex(number)
print (hexOutput)
