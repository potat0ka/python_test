# import random

# random_number = random.randint(1,100)
# print(random_number)

import random
random_number = random.randint(1, 100)
print(f"The correct number is: {random_number94}")
print("Guessing Game! ")
print("Enter random number between 1 and 100. ")
while True:
    guess = int(input("Enter your number: "))
if guess < random_number:
    print("Too low! Try again.")
elif guess > random_number:
    print("Too high! Try again.")
else:
    print(f"Congratulations! You guessed the correct number {random_number}.")  
  