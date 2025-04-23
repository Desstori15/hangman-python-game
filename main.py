import random
import os

# Hangman
HANGMAN_PICS = [
    """
    --------
    |      |
    |
    |
    |
    |
    |
    -------------
    """,
    """
    --------
    |      |
    |      O
    |
    |
    |
    |
    -------------
    """,
    """
     --------
     |      |
     |      O
     |      |
     |
     |
     |
     -------------
     """,
    """
        --------
        |      |
        |      O
        |     /|
        |
        |
        |
        -------------
        """,
    """
          --------
          |      |
          |      O
          |     /|\\
          |
          |
          |
          -------------
          """,
    """
           --------
           |      |
           |      O
           |     /|\\
           |      |
           |     /
           |
           -------------
           """,
    """
              --------
              |      |
              |      O
              |     /|\\
              |      |
              |     / \\
              |
              -------------
              """
]

# Load words from a file or use a default list
def load_words(filename="words.txt"):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            words = [line.strip().lower() for line in file if line.strip()]
            if words:
                return words
    # fallback
    return ['python', 'hangman', 'program', 'developer', 'console', 'random', 'string', 'variable', 'function', 'loop']


# Choose a random word from the list
def choose_word(word_list):
    return random.choice(word_list)

# Display the current state of the word
def display_word(word, guessed_letters):
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])

# Get a valid guess from the user
def get_guess(used_letters):
    while True:
        guess = input("Enter a letter: ").lower()
        if len(guess) == 1 and guess.isalpha() and guess not in used_letters:
            return guess
        print("Invalid input or letter already used. Try again.")

# Main game function
def play_game(words):
    word = choose_word(words)
    guessed_letters = []
    wrong_guesses = 0
    max_wrong = len(HANGMAN_PICS) - 1

    while wrong_guesses < max_wrong and display_word(word, guessed_letters) != word:
        print(HANGMAN_PICS[wrong_guesses])
        print("Used letters:", ', '.join(guessed_letters))
        print("Current word:", display_word(word, guessed_letters))

        guess = get_guess(guessed_letters)
        guessed_letters.append(guess)

        if guess not in word:
            print("Wrong guess!")
            wrong_guesses += 1
        else:
            print("Good guess!")

    if display_word(word, guessed_letters) == word:
        print("\nYou won! The word was:", word)
        return True
    else:
        print(HANGMAN_PICS[wrong_guesses])
        print("\nYou lost! The word was:", word)
        return False

# Main loop with win/loss counter
def main():
    word_list = load_words()
    wins = 0
    losses = 0

    while True:
        print("\n=-=-= New Game =-=-=")
        if play_game(word_list):
            wins += 1
        else:
            losses += 1

        print(f"Wins: {wins}, Losses: {losses}")
        again = input("Do you want to play again? (yes/no): ")
        if again != 'yes':
            break

    print("Thanks for playing!")

if __name__ == "__main__":
    main()
