import random

def generate_number():
    number = random.randint(1000, 9999)
    return str(number)

def get_guess():
    while True:
        guess = input("Enter your 4-digit guess: ")
        if len(guess) == 4 and guess.isdigit():
            return guess
        else:
            print("Invalid input. Please enter a 4-digit number.")

def calculate(number, guess):
    mouse = 0
    men = 0
    for i in range(4):
        if guess[i] == number[i]:
            mouse += 1
        elif guess[i] in number:
            men += 1
    return mouse, men

def play_game():
    number = generate_number()
    guesses = 0
    print("Welcome to Mouse and Men!")

    while True:
        guess = get_guess()
        guesses += 1
        mouse, men = calculate(number, guess)

        mouse_str = "mouse" if mouse != 1 else "mouse"
        men_str = "men" if men != 1 else "man"

        print(f"You have {mouse} {mouse_str} and {men} {men_str}.")

        if mouse == 4:
            print(f"Congratulations! You guessed the number in {guesses} guesses.")
            break

if __name__ == "__main__":
    play_game()