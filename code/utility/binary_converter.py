number = input("Enter denary number: ")
while not number.isdigit():
  number = input("Enter denary number: ")
number = int(number)
binary = bin(number)
print (binary)
