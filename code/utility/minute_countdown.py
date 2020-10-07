import time

minutes = input("How many minutes would you like to countdown from?: ")
while not minutes.isdigit():
  minutes = input("How many minutes would you like to countdown from?: ")
minutes = int(minutes)

countdown = minutes * 60


while not countdown == 0:
  print (countdown)
  countdown -= 1
  time.sleep(1)
print ("Countdown complete")
