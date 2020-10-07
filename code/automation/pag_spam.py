import time
import pyautogui

message = input("Enter message to send: ")
messages = input("Enter number of messages:")
while not messages.isdigit():
  messages = input("Enter number of messages:")
messages = int(messages)

print ("Started, activating first protocol in 5 seconds")
time.sleep(5)


while messages > 0:
  pyautogui.click()
  pyautogui.typewrite(message)
  pyautogui.Enter()
  time.sleep(0.5)
print ("Operation finished")