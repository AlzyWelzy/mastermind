import random

COLORS = ["R", "G", "B", "B", "W", "S"]
TRIES = 10
CODE_LENGTH = 4


def generate_code():
    code = []
    for _ in range(CODE_LENGTH):
        color = random.choice(COLORS)
        code.append(color)
    # print(code)
    return code


code = generate_code()


def guess_code():
    while True:
        guess = input("Guess: ").upper().split(" ")

        if len(guess) != CODE_LENGTH:
            print(f"YOU MUST GET {CODE_LENGTH} COLORS.")
            continue

        for color in guess:
            if color not in COLORS:
                print(f"Invalid color: {color}. Try again.")
        else:
            break
    return guess


def check_code(guess, real_code):
    color_counts = {}
    correct_pos = 0
    incorrect_pos = 0

    for color in real_code:
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] += 1

    for guess_color, real_color in zip(guess, real_code):
        if guess_color == real_color:
            correct_pos += 1
            # color_counts += 1
            color_counts[guess_color] -= 1

    for guess_color, real_color in zip(guess, real_color):
        if guess_color in color_counts and color_counts[guess_color] > 0:
            incorrect_pos += 1
            color_counts[guess_color] -= 1

    return correct_pos, incorrect_pos


def game():
    print(f"WELCOME TO mastermind, you have {TRIES} to guess the code...")
    print("The valid colors are", *COLORS)
    code = generate_code()

    for attempts in range(1, TRIES + 1):
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)

        if correct_pos == CODE_LENGTH:
            print(f"You guessed the code in {attempts} tries!")
            break

        print(
            f"Correct Positions: {correct_pos} | Incorrect Positions: {incorrect_pos}"
        )
    else:
        print("You ran out of tries, the code was:", *code)


if __name__ == "__main__":
    while True:
        game()
        again = input("Would you love to play gain? (y/n): ")

        if again.lower() == "n":
            break
