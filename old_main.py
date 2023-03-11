import random
from typing import List, Tuple

COLORS = ["R", "G", "B", "B", "W", "S"]
TRIES = 10
CODE_LENGTH = 4


class Game:
    def __init__(self):
        self.code = self.generate_code()

    @staticmethod
    def generate_code() -> List[str]:
        code = []
        for _ in range(CODE_LENGTH):
            color = random.choice(COLORS)
            code.append(color)
        # print(code)
        return code

    @staticmethod
    def guess_code() -> List[str]:
        while True:
            guess = input("Guess: ").upper().split(" ")

            if len(guess) != CODE_LENGTH:
                print(f"YOU MUST GET {CODE_LENGTH} COLORS.")
                continue

            invalid_colors = [color for color in guess if color not in COLORS]
            if invalid_colors:
                print(f"Invalid colors: {invalid_colors}. Try again.")
                continue

            break

        return guess

    @staticmethod
    def check_code(guess: List[str], real_code: List[str]) -> Tuple[int, int]:
        color_counts = {}
        correct_pos = 0
        incorrect_pos = 0

        for color in real_code:
            color_counts[color] = color_counts.get(color, 0) + 1

        for guess_color, real_color in zip(guess, real_code):
            if guess_color == real_color:
                correct_pos += 1
                color_counts[guess_color] -= 1

        for guess_color, real_color in zip(guess, real_code):
            if guess_color in color_counts and color_counts[guess_color] > 0:
                incorrect_pos += 1
                color_counts[guess_color] -= 1

        return correct_pos, incorrect_pos

    def play(self) -> bool:
        print(f"WELCOME TO mastermind, you have {TRIES} to guess the code...")
        print("The valid colors are", *COLORS)

        for attempt in range(1, TRIES + 1):
            guess = self.guess_code()
            correct_pos, incorrect_pos = self.check_code(guess, self.code)

            if correct_pos == CODE_LENGTH:
                print(f"You guessed the code in {attempt} tries!")
                return True

            print(
                f"Correct Positions: {correct_pos} | Incorrect Positions: {incorrect_pos}"
            )

        print("You ran out of tries, the code was:", *self.code)
        return False


def main() -> None:
    while True:
        game = Game()
        success = game.play()
        again = input("Would you love to play gain? (y/n): ")

        if again.lower() == "n":
            break


if __name__ == "__main__":
    main()
