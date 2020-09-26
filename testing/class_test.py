class Member:
	def __init__(self, name, role):
		self.name = name
		self.role = role
		
userName = input("What is your name? ")
userRole = input("What is your role? ")

user = Member(userName, userRole)
print (user.name, "is", user.role)
