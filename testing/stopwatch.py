# This does not work yet, there is not much point trying to run it.

import time
import keyboard

print ("Press 's' to start the stopwatch")

def main():
	while True:
		try:
			if keyboard.is_pressed('s'):
				startTime = time.time()
				print ("Stopwatch has started!")
				print ("Press 'p'' to stop it.")
			elif keyboard.is_pressed('p'):
				stopTime = time.time()
			print ("Stopwatch stopped!")
			totalTime = startTime - stopTime 
			print (totalTime)
		except:
			print("Bad input")
		main()
