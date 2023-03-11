import random


class Mastermind:
    def __init__(self, colors, code_length, tries):
        self.colors = colors
        self.code_length = code_length
        self.tries = tries
        self.secret_code = None

    def generate_code(self):
        self.secret_code = []
        for _ in range(self.code_length):
            color = random.choice(self.colors)
            self.secret_code.append(color)

    def guess_code(self, guess):
        guess = guess.upper().split()
        if len(guess) != self.code_length:
            raise ValueError(f"You must guess {self.code_length} colors.")
        for color in guess:
            if color not in self.colors:
                raise ValueError(f"Invalid color: {color}.")
        return guess

    def check_code(self, guess):
        correct_pos = 0
        incorrect_pos = 0
        secret_code_counts = {}
        guess_counts = {}
        for i in range(self.code_length):
            if guess[i] == self.secret_code[i]:
                correct_pos += 1
            else:
                secret_code_counts[self.secret_code[i]] = (
                    secret_code_counts.get(self.secret_code[i], 0) + 1
                )
                guess_counts[guess[i]] = guess_counts.get(guess[i], 0) + 1
        for color in self.colors:
            if color in secret_code_counts and color in guess_counts:
                incorrect_pos += min(secret_code_counts[color], guess_counts[color])
        return correct_pos, incorrect_pos

    def play(self):
        print(f"WELCOME TO mastermind, you have {self.tries} to guess the code...")
        print("The valid colors are", *self.colors)
        self.generate_code()
        for attempts in range(1, self.tries + 1):
            guess = input("Guess: ")
            try:
                guess = self.guess_code(guess)
            except ValueError as e:
                print(e)
                continue
            correct_pos, incorrect_pos = self.check_code(guess)
            if correct_pos == self.code_length:
                print(f"You guessed the code in {attempts} tries!")
                return
            print(
                f"Correct Positions: {correct_pos} | Incorrect Positions: {incorrect_pos}"
            )
        print("You ran out of tries, the code was:", *self.secret_code)


def main():
    colors = ["R", "G", "B", "B", "W", "S"]
    code_length = 4
    tries = 10
    game = Mastermind(colors, code_length, tries)
    game.play()


if __name__ == "__main__":
    main()
