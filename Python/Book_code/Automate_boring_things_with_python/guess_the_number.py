# Guess the number
import random
secret = random.randint(1,20)
print("I'm thinking of a number between 1 and 20.")

# Ask the player to guess 6 times
for guessesTaken in range(6):
    print("Take a guess.")
    guess = int(input())

    if guess > secret:
        print("Your guess is too high.")
    elif guess < secret:
        print("Your guess is too low")
    else :
        break

if guess == secret:
    print(f"Good job! You have guessed my number in {guessesTaken} guesses!")
else :
    print("Nope. The number I was thinking was" + str(secret))