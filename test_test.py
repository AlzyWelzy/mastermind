import random


class Code:
    def __init__(self, num_colors):
        self.colors = ["R", "G", "B", "Y", "O", "P"][:num_colors]
        self.secret_code = []

    def generate_code(self, length):
        self.secret_code = [random.choice(self.colors) for _ in range(length)]

    def check_code(self, guess):
        correct_positions = 0
        correct_colors = 0
        for i, color in enumerate(guess):
            if color == self.secret_code[i]:
                correct_positions += 1
            elif color in self.secret_code:
                correct_colors += 1
        return correct_positions, correct_colors


class Game:
    def __init__(self):
        self.colors = ["R", "G", "B", "Y", "O", "P"]
        self.num_positions = 4
        self.num_guesses = 10

    def play_game(self):
        self.print_instructions()
        code = self.generate_code()
        for i in range(self.num_guesses):
            guess = self.get_guess(i)
            result = self.check_code(guess, code)
            self.print_result(result)
            if result == (self.num_positions, 0):
                self.print_win_message()
                return
        self.print_lose_message(code)

    def print_instructions(self):
        print("Welcome to Mastermind!")
        print(
            f"I'm thinking of a {self.num_positions}-color code using the colors {', '.join(self.colors)}"
        )
        print(f"You have {self.num_guesses} guesses to crack the code. Good luck!")

    def generate_code(self):
        return [random.choice(self.colors) for _ in range(self.num_positions)]

    def get_guess(self, guess_num):
        while True:
            guess = input(f"Guess #{guess_num + 1}: ")
            if self.is_valid_guess(guess):
                return guess
            print("Invalid guess! Please try again.")

    def is_valid_guess(self, guess):
        if len(guess) != self.num_positions:
            return False
        for color in guess:
            if color not in self.colors:
                return False
        return True

    def check_code(self, guess, code):
        correct_positions = 0
        correct_colors = 0
        for i, color in enumerate(guess):
            if color == code[i]:
                correct_positions += 1
            elif color in code:
                correct_colors += 1
        return correct_positions, correct_colors

    def print_result(self, result):
        correct_positions, correct_colors = result
        print(f"Correct positions: {correct_positions}")
        print(f"Correct colors: {correct_colors}")

    def print_win_message(self):
        print("Congratulations! You cracked the code!")

    def print_lose_message(self, code):
        print(f"Sorry, you ran out of guesses. The code was {''.join(code)}")


while True:
    num_colors = int(input("Enter the number of colors to use (2-6): "))
    code_length = int(input("Enter the length of the secret code (2-6): "))
    max_guesses = int(input("Enter the maximum number of guesses (1-12): "))

    game = Game(num_colors, code_length, max_guesses)
    game.play_game()
