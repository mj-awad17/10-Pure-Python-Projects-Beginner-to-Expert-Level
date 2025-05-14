import random

# Step 1: Generate random number
secret_number = random.randint(1, 100)

# Step 2: Greet the player
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# Step 3: Start guessing loop
guess = None
attempts = 0

while guess != secret_number:
    try:
        guess = int(input("Take a guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
    except ValueError:
        print("Please enter a valid number!")

# Step 4: Win message
print(f"Congratulations! You guessed the number in {attempts} tries.")
