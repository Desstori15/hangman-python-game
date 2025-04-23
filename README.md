#  hangman-python-game

A colorful terminal-based **Hangman game** written in Python 🐍 with difficulty levels, ASCII art visuals, and word loading from file.

---

##  Features

- ✅ Difficulty levels: easy / normal / hard
- ✅ Word guessing letter-by-letter or whole word
- ✅ Colorful feedback using `colorama`
- ✅ ASCII hangman visuals for every wrong guess
- ✅ Word list from file (`words.txt`) or defaults
- ✅ Win/loss tracking and replay support

---
##  Project Structure

```
hangman-python-game/
├── hangman.py       # Game logic and UI
├── main.py          # Entry point (calls hangman.main())
├── words.txt        # Optional word list
├── .gitignore
└── README.md        # You're here!
```


---

##  Requirements

- Python 3.7+
- colorama (`pip install colorama`)

---

##  How to Run

```bash
# 1. Clone the repository
git clone https://github.com/Desstori15/hangman-python-game.git
cd hangman-python-game

# 2. (Optional) create a virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate

# 3. Install dependencies
pip install colorama

# 4. Run the game
python main.py
```


## 📝 Example Gameplay
Choose difficulty: easy / normal / hard
Difficulty: easy

=-=-= New Game =-=-=
Used guesses: a, s
Word: p _ _ t _ _

Good guess!
Wrong guess!
You won! The word was: python
Wins: 1, Losses: 0
Do you want to play again? (yes/no): no
Thanks for playing!


 ## Custom Words
You can add your own words by editing the words.txt file (one word per line, all lowercase).
If no file is found, a default word list is used.

## 👨‍💻 Author
Vladislav Dobriyan
GitHub: @Desstori15
