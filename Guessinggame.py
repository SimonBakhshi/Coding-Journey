# Creating a guessing the number game:
import random
secret_number = random.randint(1,20)
print("Hello my friend! I am thinking of a random number between 1 and 20.")

# Ask the player to guess 6 times code:
for guesses_taken in range(1, 7):
    print("Take a guess :-)")
    guess = int(input())

    if guess < secret_number:
        print("Your guess is too low my friend")
    elif guess > secret_number:
        print("your guess is to high friend")
    else:
        break # This condition is the correct guess!
if guess == secret_number:
    print("Good job my friend! You guessed my number in " + str(guesses_taken) + " guesses")
else:
    print("Sorry my friend. The number i was thinking of was " + str(secret_number))