import time

t = input("Enter start time: ")
while not t.isdigit():
    t = input("Enter start time: ")
t = int(t)
print (t)

while t:
    timer = t
    time.sleep(1)
    t -= 1
    print (t)

print ("Countdown finished!")
