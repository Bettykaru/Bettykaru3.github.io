# See the Instructions tab
import random
# Set secret number
secret_number = random.randint(1, 99)
print("I'm thinking of a number between 1 and 99")

# Ask the user to guess 
guess_no =int(input("Guess the number: "))
# Check to see if the guess is <, >, or = secret number  

while guess_no != secret_number:
  guess_no = int(input("Guess the number: "))
  if guess_no == secret_number:
    print(f"Congrats! The number was {secret_number} ")
  elif guess_no > secret_number :
    print("Your guess is too high")
  elif guess_no < secret_number :
    print("Your guess is too low")
  elif guess_no != secret_number.isdecimal():
    print("that's not a number")


  
# Print the right message