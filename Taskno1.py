Taskno:-1

import random

print("🎯 Welcome to Guess the Number Game!")
print("I have selected a number between 1 and 10.")
secret_number = random.randint(1, 10)
attempts = 0
while True:
    guess = int(input("Enter your guess: "))
    attempts += 1
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("🎉 Congratulations! You guessed it right.")
        print("Total attempts:", attempts)
        break
Output:-
🎯 Welcome to Guess the Number Game!
I have selected a number between 1 and 10.
Enter your guess: 1
Too low! Try again.
Enter your guess: 3
Too low! Try again.
Enter your guess: 66
Too high! Try again.
Enter your guess:

