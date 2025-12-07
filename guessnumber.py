import random

def play_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    player_guess = None

    print("Welcome to the Number Guessing Game!")
    print(f"You have {max_attempts} attempts to guess the number between 1 and 100.")

    while player_guess != number_to_guess and attempts < max_attempts:
        try:
            player_guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        attempts += 1

        if player_guess < number_to_guess:
            print("Too low!")
        elif player_guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts!")
            break
    else:
        if player_guess != number_to_guess:
            print(f"Sorry! You've used all {max_attempts} attempts. The number was {number_to_guess}.")

# Main loop for replaying the game
while True:
    play_game()
    replay = input("Do you want to play again? (yes/no): ").lower()
    if replay != "yes":
        print("Thanks for playing! Goodbye.")
        break
