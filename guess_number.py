import random
import sys

print("Welcome to the Number Guessing Game!")

def guess(low, high):
    if low > high:
        print("Error: Lower limit cannot be greater than higher limit, please try again.")
        return

    random_number = random.randint(low, high)
    guess = 0
    while guess != random_number:
        guess = int(input(f"What number am I thinking of between {low} and {high}: "))
        if guess < random_number:
            print("Sorry! Your guess was too low. Try again.")
        elif guess > random_number:
            print("Sorry! Your guess was too high. Try again.")
    print(f"Nice! You got the random number, {random_number}. Give yourself a pat on the back.")
    sys.exit()

while True: 
    lower_limit = int(input("Please enter the lower limit of your guess range: "))
    higher_limit = int(input("Now enter the higher limit of your guess range: "))

    guess(lower_limit, higher_limit)