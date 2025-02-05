import random

some_words = ["python", "java", "kotlin", "javascript"]

# Randomly choose a word from the list
word = random.choice(some_words)
print("H A N G M A N")

if __name__ == '__main__':
    print("Guess the word! Hint: word is a programming language")

    # Display initial blank word
    display_word = ['_'] * len(word)
    print(' '.join(display_word))

    guessed_letters = set()
    tries = len(word) + 2  # Number of tries based on word length
    correct_guesses = 0

    while tries > 0:
        print(f"\nTries left: {tries}")
        guess = input("Enter a letter: ").lower()

        # Validate the input
        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("You have already guessed that letter.")
            continue

        guessed_letters.add(guess)

        # Check if the guessed letter is in the word
        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
            for i, letter in enumerate(word):
                if letter == guess:
                    display_word[i] = guess
                    correct_guesses += 1
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            tries -= 1

        # Display the current state of the word
        print(' '.join(display_word))

        # Check if the word has been fully guessed
        if correct_guesses == len(word):
            print("Congratulations, You won!")
            break

    if tries == 0:
        print("\nYou ran out of tries.")
        print(f"The word was '{word}'.")
        print("Better luck next time!")