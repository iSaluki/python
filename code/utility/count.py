start = input("Count from: ")
while not start.isdigit():
	start = input("Count from: ")
start = int(start)
stop = input("Count to: ")
while not stop.isdigit():
	stop = input("Count to: ")
stop = int(stop)
stop += 1
for n in range(start, stop):
	print(n)
