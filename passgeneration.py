import random
import string

#define password length
password_length = 10
user = input("enter random password: ")

#define possible characters
characters = string.ascii_letters + string.digits + string.punctuation
  
#generate te password from the set of characters 
password = ''.join(random.choice(characters) for i in range(password_length))
print ("that is the password!")
