
# NURDLE

## Description
This is a project I created when I started Learning Python. NURDLE is a number-guessing game inspired by Wordle, but with numbers! The player tries to guess a randomly generated number of a specified length, with feedback on each guess to indicate digit correctness and position.

## Table of Contents
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Game Rules](#game-rules)
- [Features](#features)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Authors](#authors)
- [Acknowledgments](#acknowledgments)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Har-Var/Nurdle.git
   cd NURDLE
   ```
2. Ensure you have Python 3.x installed.
3. No additional dependencies are required.

## Usage
Run the game with:
```bash
python nurdle.py
```

## Game Rules
1. Select the length of the number (between 2 and 10 digits).
2. Guess the number within a limited number of attempts (one more than the chosen length).
3. After each guess, symbols indicate:
   - `✓` - Correct digit in the correct position.
   - `?` - Correct digit in a different position.
   - `✗` - Incorrect digit.

Example:
If the number is `65343` and your guess is `61932`, the result will show:
```
Your Guess: 6 1 9 3 2
Result:     ✓ ✗ ✗ ? ✗
```

## Features
- Dynamic game length based on user input.
- Provides feedback for each digit position.
- Replay option at the end of the game.

## Project Structure
- `nurdle.py`: Main script containing the game logic, user prompts, and results display.

## Contributing
Contributions are welcome! Please submit a pull request with any improvements.

## License
This project is licensed under the MIT License.

## Authors
- [Har-Var](https://github.com/Har-Var)

## Acknowledgments
Thanks to Wordle for the inspiration and to everyone who provided feedback on this project!
