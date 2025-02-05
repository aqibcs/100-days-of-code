# Hangman Game

Welcome to the **Hangman Game**! This is a simple Python-based implementation of the classic word-guessing game. The game randomly selects a programming language as the target word, and the player must guess the word by suggesting letters within a limited number of tries.

---

## Table of Contents
1. [How to Play](#how-to-play)
2. [Features](#features)
3. [Installation](#installation)
4. [Running the Game](#running-the-game)

---

## How to Play

1. The game randomly selects a word from a predefined list of programming languages.
2. The player is shown a series of underscores (`_`) representing each letter in the word.
3. The player guesses one letter at a time.
4. If the guessed letter is in the word, it is revealed in its correct position(s).
5. If the guessed letter is not in the word, the player loses one try.
6. The game continues until:
   - The player guesses all the letters in the word correctly (win), or
   - The player runs out of tries (lose).

---

## Features

- **Random Word Selection**: The game randomly selects a word from a list of programming languages.
- **Interactive Gameplay**: The player interacts with the game by entering single-letter guesses.
- **Tries Counter**: The player has a limited number of tries to guess the word.
- **Immediate Feedback**: The game provides immediate feedback on whether a guessed letter is correct or not.
- **Winning and Losing Conditions**: The game clearly indicates when the player wins or loses.

---

## Installation

To run this game, you need to have Python installed on your system. If you don't have Python installed, you can download it from [python.org](https://www.python.org/).

---

## Running the Game

1. Open a terminal or command prompt.
2. Navigate to the directory containing the `hangman.py` file.
3. Run the game using the following command:

   ```bash
   python hangman.py