# Mastermind Game

This is a Python implementation of the classic board game Mastermind. The objective of the game is to guess a randomly generated code consisting of 4 colors, each chosen from a pool of 6 colors, in 10 or fewer tries.

## Installation and Usage

1. Clone the repository or download the `main.py` file.
2. Open a terminal or command prompt and navigate to the directory containing the `main.py` file.
3. Run the command `python main.py` to start the game.
4. Follow the on-screen prompts to play the game.

## Game Rules

1. The computer generates a random 4-color code from the 6 available colors.
2. The player has 10 or fewer tries to guess the code.
3. The player enters a guess consisting of 4 colors, each separated by a space.
4. If the player enters an incorrect number of colors, an error message is displayed and the player is prompted to try again.
5. If the player enters an invalid color, an error message is displayed and the player is prompted to try again.
6. After each guess, the computer provides feedback on the accuracy of the guess.
7. The feedback consists of two numbers:
   - The number of colors in the correct position (marked as 'Correct Positions')
   - The number of colors in the incorrect position (marked as 'Incorrect Positions')
8. The game ends when the player guesses the code correctly or runs out of tries.

## License

This project is licensed under the GNU Affero General Public License v3.0 (AGPLv3). See the [LICENSE](LICENSE) file for details.

## Author

This project was created by AlzyWelzy. Follow me on [GitHub](https://github.com/AlzyWelzy).
