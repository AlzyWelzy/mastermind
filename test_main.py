import random
from typing import List, Tuple


class Game:
    COLORS = ["R", "G", "B", "B", "W", "S"]
    TRIES = 10
    CODE_LENGTH = 4

    def __init__(self):
        self.code = self.generate_code()

    @classmethod
    def generate_code(cls) -> List[str]:
        code = []
        for _ in range(cls.CODE_LENGTH):
            color = random.choice(cls.COLORS)
            code.append(color)
        # print(code)
        return code

    @classmethod
    def guess_code(cls) -> List[str]:
        while True:
            guess = input("Guess: ").upper().split(" ")

            if len(guess) != cls.CODE_LENGTH:
                print(f"YOU MUST GET {cls.CODE_LENGTH} COLORS.")
                continue

            invalid_colors = [color for color in guess if color not in cls.COLORS]
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
                color_counts[real_color] -= 1

        for guess_color, real_color in zip(guess, real_code):
            if (
                guess_color in color_counts
                and color_counts[guess_color] > 0
                and guess_color != real_color
            ):
                incorrect_pos += 1
                color_counts[guess_color] -= 1

        return correct_pos, incorrect_pos

    def play(self) -> None:
        print(f"WELCOME TO mastermind, you have {self.TRIES} to guess the code...")
        print("The valid colors are", *self.COLORS)

        for attempt in range(1, self.TRIES + 1):
            guess = self.guess_code()
            correct_pos, incorrect_pos = self.check_code(guess, self.code)

            if correct_pos == self.CODE_LENGTH:
                print(f"You guessed the code in {attempt} tries!")
                break

            print(
                f"Correct Positions: {correct_pos} | Incorrect Positions: {incorrect_pos}"
            )

        else:
            print("You ran out of tries, the code was:", *self.code)

    def __str__(self):
        return f"Code: {self.code}"


def main() -> None:
    while True:
        mastermind = Game()
        mastermind.play()
        again = input("Would you like to play again? (y/n): ")

        if again.lower() == "n":
            break


if __name__ == "__main__":
    main()
