# code_alpha-Tasks-
# Hangman Game 🎮

A classic word-guessing game implemented in Python where players try to guess a hidden word letter by letter.

## 🎯 How to Play

1. The game randomly selects a word from a predefined list
2. You see the word represented as underscores (one for each letter)
3. Guess letters one at a time
4. Correct guesses reveal the letter's position(s) in the word
5. Incorrect guesses count against you (6 wrong guesses allowed)
6. Win by guessing all letters before running out of attempts!

## 🚀 Getting Started

### Prerequisites
- Python 3.11 or higher

### Running the Game
1. Clone this repository
2. Run the game:
   ```bash
   python main.py
   ```

## 🎮 Game Features

- **5 Predefined Words**: python, computer, hangman, coding, replit
- **Input Validation**: Ensures only single letters are accepted
- **Progress Tracking**: Shows guessed letters and remaining attempts
- **Play Again Option**: Continue playing multiple rounds
- **User-Friendly Interface**: Clear prompts and feedback

## 📝 Game Rules

- You have 6 incorrect guesses before losing
- Only single alphabetic characters are accepted
- Previously guessed letters cannot be guessed again
- The game is case-insensitive

## 🎲 Sample Gameplay

```
Welcome to Hangman!
The word has 6 letters.
You have 6 incorrect guesses allowed.

Word: _ _ _ _ _ _
Guessed letters: 
Incorrect guesses remaining: 6
Guess a letter: p

Good guess! 'p' is in the word.

Word: p _ _ _ _ _
Guessed letters: p
Incorrect guesses remaining: 6
Guess a letter: y

Good guess! 'y' is in the word.
```

## 🛠️ Code Structure

- `hangman()`: Main game logic
- `play_again()`: Handles replay functionality
- Input validation for user guesses
- Random word selection from predefined list

## 🔧 Customization

Want to add more words? Simply modify the `words` list in the `hangman()` function:

```python
words = ["python", "computer", "hangman", "coding", "replit", "your_word_here"]
```
