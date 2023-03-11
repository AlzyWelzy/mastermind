import random


class Mastermind:
    def __init__(self, num_colors=6, code_length=4, num_guesses=10):
        self.num_colors = num_colors
        self.code_length = code_length
        self.num_guesses = num_guesses
        self.colors = ["R", "G", "B", "Y", "O", "P"][:num_colors]
        self.winning_code = self.generate_code()

    def generate_code(self):
        code = []
        for _ in range(self.code_length):
            code.append(random.choice(self.colors))
        return code

    def check_code(self, guess):
        exact_matches = 0
        color_matches = 0
        unmatched_guesses = []
        unmatched_winning_codes = []

        for i in range(self.code_length):
            if guess[i] == self.winning_code[i]:
                exact_matches += 1
            else:
                unmatched_guesses.append(guess[i])
                unmatched_winning_codes.append(self.winning_code[i])

        for color in self.colors:
            guess_count = unmatched_guesses.count(color)
            winning_code_count = unmatched_winning_codes.count(color)
            color_matches += min(guess_count, winning_code_count)

        return exact_matches, color_matches

    def is_valid_guess(self, guess):
        if len(guess) != self.code_length:
            print(
                f"Invalid guess. Please enter a guess that is {self.code_length} characters long."
            )
            return False

        for color in guess:
            if color.upper() not in self.colors:
                print(f"Invalid guess. Please only use the colors {self.colors}.")
                return False

        return True

    def play_game(self):
        print(
            f"Guess the {self.code_length}-letter code in {self.num_guesses} tries, using the colors {self.colors}"
        )
        for i in range(self.num_guesses):
            guess = input(f"Guess {i+1}: ")
            if not guess:
                print("Invalid guess. Please enter a guess.")
                continue

            guess = list(guess.upper())
            if not self.is_valid_guess(guess):
                continue

            exact_matches, color_matches = self.check_code(guess)
            print(
                f"Result: {exact_matches} exact matches, {color_matches} color matches"
            )
            if guess == self.winning_code:
                print("Congratulations! You guessed the code!")
                play_again = input("Do you want to play again? (y/n): ")
                if play_again.lower() == "y":
                    self.winning_code = self.generate_code()
                    print("\n")
                    self.play_game()
                else:
                    return
        print(
            f"Sorry, you ran out of guesses. The winning code was {self.winning_code}"
        )
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() == "y":
            self.winning_code = self.generate_code()
            print("\n")
            self.play_game()


if __name__ == "__main__":
    game = Mastermind(num_colors=4, code_length=5, num_guesses=12)
    game.play_game()
