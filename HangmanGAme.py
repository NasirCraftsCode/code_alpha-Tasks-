
import random

def hangman():
    # List of 5 predefined words
    words = ["python", "computer", "hangman", "coding", "replit"]
    
    # Choose a random word
    word = random.choice(words).lower()
    word_letters = set(word)
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect = 6
    
    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters.")
    print("You have 6 incorrect guesses allowed.\n")
    
    while len(word_letters) > 0 and incorrect_guesses < max_incorrect:
        # Display current progress
        word_progress = [letter if letter in guessed_letters else '_' for letter in word]
        print(f"Word: {' '.join(word_progress)}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
        print(f"Incorrect guesses remaining: {max_incorrect - incorrect_guesses}")
        
        # Get user input
        guess = input("Guess a letter: ").lower()
        
        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
            
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
            
        # Process the guess
        guessed_letters.add(guess)
        
        if guess in word_letters:
            word_letters.remove(guess)
            print(f"Good guess! '{guess}' is in the word.\n")
        else:
            incorrect_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.\n")
    
    # Game over - check if won or lost
    if len(word_letters) == 0:
        print(f"Congratulations! You guessed the word: {word}")
    else:
        print(f"Game over! The word was: {word}")

def play_again():
    while True:
        choice = input("Do you want to play again? (y/n): ").lower()
        if choice in ['y', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False
        else:
            print("Please enter 'y' or 'n'.")

if __name__ == "__main__":
    while True:
        hangman()
        if not play_again():
            print("Thanks for playing!")
            break
