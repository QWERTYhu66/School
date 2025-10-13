import random

secret_number = random.randint(1, 100)
guesses_left = 5
guessed_numbers = []
insults = [
    "Really? Try harder.",
    "Are you even trying?",
    "That's just embarrassing.",
    "My pet could guess better.",
    "Hopeless!"
]

while guesses_left > 0:
    try:
        guess = int(input(f"Guess the number (between 1 and 100). You have {guesses_left} guesses left: "))
    except ValueError:
        print("That's not even a number. Wow.")
        continue

    guessed_numbers.append(guess)

    if guess == secret_number:
        print("YAY! You guessed it!")
        break
    else:
        print("NO!", end=' ')
        if guess < secret_number:
            print("Too low.", end=' ')
        else:
            print("Too high.", end=' ')
        print(insults[5 - guesses_left])
        guesses_left -= 1

if guesses_left == 0 and guess != secret_number:
    print(f"Out of guesses! The number was {secret_number}.")

print("Your guesses were: ", guessed_numbers)