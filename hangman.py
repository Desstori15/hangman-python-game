import random
import os
from colorama import init, Fore, Style

# Initialize colorama
init()

# Hangman ASCII Art
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

# Load words

def load_words(filename="words.txt"):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            words = [line.strip().lower() for line in file if line.strip()]
            if words:
                return words
    return ['python', 'hangman', 'program', 'developer', 'console', 'random', 'string', 'variable', 'function', 'loop']


def choose_word(word_list, difficulty):
    if difficulty == 'easy':
        filtered = [word for word in word_list if len(word) <= 5]
        return random.choice(filtered if filtered else word_list)
    elif difficulty == 'hard':
        filtered = [word for word in word_list if len(word) >= 7]
        return random.choice(filtered if filtered else word_list)
    return random.choice(word_list)


def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])


def get_guess(used_letters):
    while True:
        guess = input("Enter a letter or try guessing the full word: ").lower()
        if guess.isalpha():
            if guess in used_letters:
                print("You already used that letter or word. Try again.")
            else:
                return guess
        else:
            print("Invalid input. Enter only letters.")


def play_game(words, difficulty):
    word = choose_word(words, difficulty)
    guessed_letters = []
    wrong_guesses = 0
    max_wrong = len(HANGMAN_PICS) - 1
    used_guesses = []

    while wrong_guesses < max_wrong and display_word(word, guessed_letters).replace(' ', '') != word:
        print(Fore.YELLOW + HANGMAN_PICS[wrong_guesses] + Style.RESET_ALL)
        print("Used guesses:", ', '.join(used_guesses))
        print("Word:", display_word(word, guessed_letters))

        guess = get_guess(used_guesses)
        used_guesses.append(guess)

        if len(guess) > 1:
            if guess == word:
                print(Fore.GREEN + "Correct! You guessed the full word!" + Style.RESET_ALL)
                return True
            else:
                print(Fore.RED + "Wrong full-word guess!" + Style.RESET_ALL)
                wrong_guesses += 1
        elif guess in word:
            print(Fore.GREEN + "Good guess!" + Style.RESET_ALL)
            guessed_letters.append(guess)
        else:
            print(Fore.RED + "Wrong guess!" + Style.RESET_ALL)
            wrong_guesses += 1

    if display_word(word, guessed_letters).replace(' ', '') == word:
        print(Fore.GREEN + f"\nYou won! The word was: {word}" + Style.RESET_ALL)
        return True
    else:
        print(Fore.RED + HANGMAN_PICS[wrong_guesses] + Style.RESET_ALL)
        print(Fore.RED + f"\nYou lost! The word was: {word}" + Style.RESET_ALL)
        return False


def main():
    word_list = load_words()
    wins = 0
    losses = 0

    print("Choose difficulty: easy / normal / hard")
    difficulty = input("Difficulty: ").lower()
    if difficulty not in ['easy', 'normal', 'hard']:
        difficulty = 'normal'

    while True:
        print("\n=-=-= New Game =-=-=")
        if play_game(word_list, difficulty):
            wins += 1
        else:
            losses += 1

        print(f"Wins: {wins}, Losses: {losses}")
        again = input("Do you want to play again? (yes/no): ").lower()
        if again != 'yes':
            break

    print("Thanks for playing!")


if __name__ == "__main__":
    main()
