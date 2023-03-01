#get module that generates random numbers
import random
#get random number btn 1 and 9
random_number = random.randint(1, 9)
#initialize the counter
count = 0
#loop until the number is correct
while True:
#get user input number
  user = int(input("enter random number: "))
#compare input to random number,,if less-too low
  if user== random_number:
    print("exactly")
#if greater-too high
  elif user>random_number:
    print("too high")
  if user<random_number:
    print("too low")

