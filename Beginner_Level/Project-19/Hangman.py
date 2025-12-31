"""
Hangman Game
Classic word guessing game with ASCII art and multiple difficulty levels.
"""

import random
import string

# Word categories
WORD_LISTS = {
    "easy": [
        "cat", "dog", "sun", "moon", "tree", "book", "fish", "bird",
        "star", "door", "wall", "home", "rain", "snow", "wind", "fire"
    ],
    "medium": [
        "python", "computer", "keyboard", "monitor", "program", "internet",
        "science", "history", "nature", "mountain", "ocean", "desert",
        "forest", "animal", "planet", "galaxy"
    ],
    "hard": [
        "algorithm", "programming", "artificial", "development", "encryption",
        "technology", "environment", "dictionary", "communication", "information",
        "mathematics", "architecture", "psychology", "philosophy", "engineering"
    ]
}

# Hangman ASCII art stages
HANGMAN_STAGES = [
    """
       --------
       |      |
       |      
       |     
       |      
       |     
    -------
    """,
    """
       --------
       |      |
       |      O
       |     
       |      
       |     
    -------
    """,
    """
       --------
       |      |
       |      O
       |      |
       |      
       |     
    -------
    """,
    """
       --------
       |      |
       |      O
       |     /|
       |      
       |     
    -------
    """,
    """
       --------
       |      |
       |      O
       |     /|\\
       |      
       |     
    -------
    """,
    """
       --------
       |      |
       |      O
       |     /|\\
       |     / 
       |     
    -------
    """,
    """
       --------
       |      |
       |      O
       |     /|\\
       |     / \\
       |     
    -------
    """
]


def display_hangman(tries):
    """Display the hangman based on remaining tries."""
    stage = 6 - tries
    return HANGMAN_STAGES[stage]


def display_word(word, guessed_letters):
    """Display the word with guessed letters revealed."""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


def get_difficulty():
    """Get difficulty level from user."""
    print("\n" + "=" * 60)
    print("SELECT DIFFICULTY LEVEL")
    print("=" * 60)
    print("1. Easy   (3-4 letter words)")
    print("2. Medium (5-7 letter words)")
    print("3. Hard   (8+ letter words)")
    print("=" * 60)
    
    while True:
        choice = input("\nEnter choice (1-3): ").strip()
        if choice == "1":
            return "easy"
        elif choice == "2":
            return "medium"
        elif choice == "3":
            return "hard"
        else:
            print("❌ Invalid choice. Please enter 1, 2, or 3.")


def display_game_state(word, guessed_letters, wrong_guesses, tries):
    """Display current game state."""
    print("\n" + "=" * 60)
    print(display_hangman(tries))
    print("=" * 60)
    print(f"Word: {display_word(word, guessed_letters)}")
    print(f"\nTries remaining: {tries}")
    print(f"Wrong guesses: {', '.join(sorted(wrong_guesses)) if wrong_guesses else 'None'}")
    print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
    print("=" * 60)


def play_game():
    """Main game logic."""
    # Get difficulty and select word
    difficulty = get_difficulty()
    word = random.choice(WORD_LISTS[difficulty]).lower()
    
    # Game variables
    tries = 6
    guessed_letters = set()
    wrong_guesses = set()
    
    print("\n" + "=" * 60)
    print("🎮 GAME START!")
    print("=" * 60)
    print(f"Difficulty: {difficulty.upper()}")
    print(f"Word length: {len(word)} letters")
    print(f"You have {tries} tries to guess the word!")
    
    # Game loop
    while tries > 0:
        display_game_state(word, guessed_letters, wrong_guesses, tries)
        
        # Check if word is complete
        if all(letter in guessed_letters for letter in word):
            print("\n" + "🎉" * 20)
            print(f"CONGRATULATIONS! You guessed the word: {word.upper()}")
            print("🎉" * 20)
            return True
        
        # Get user guess
        guess = input("\nGuess a letter: ").lower().strip()
        
        # Validate input
        if len(guess) != 1:
            print("⚠️  Please enter a single letter.")
            continue
        
        if guess not in string.ascii_lowercase:
            print("⚠️  Please enter a valid letter (a-z).")
            continue
        
        if guess in guessed_letters:
            print("⚠️  You already guessed that letter!")
            continue
        
        # Process guess
        guessed_letters.add(guess)
        
        if guess in word:
            print(f"✅ Correct! '{guess.upper()}' is in the word!")
        else:
            tries -= 1
            wrong_guesses.add(guess)
            print(f"❌ Wrong! '{guess.upper()}' is not in the word. {tries} tries left.")
    
    # Game over - lost
    print("\n" + display_hangman(0))
    print("\n" + "💀" * 20)
    print(f"GAME OVER! The word was: {word.upper()}")
    print("💀" * 20)
    return False


def display_stats(wins, losses):
    """Display game statistics."""
    total = wins + losses
    if total > 0:
        win_rate = (wins / total) * 100
        print("\n" + "=" * 60)
        print("📊 YOUR STATISTICS")
        print("=" * 60)
        print(f"Games played: {total}")
        print(f"Wins: {wins}")
        print(f"Losses: {losses}")
        print(f"Win rate: {win_rate:.1f}%")
        print("=" * 60)


def main():
    """Main program execution."""
    wins = 0
    losses = 0
    
    print("=" * 60)
    print("           🎮 HANGMAN GAME 🎮")
    print("=" * 60)
    print("\nGuess the word one letter at a time!")
    print("You have 6 tries before the hangman is complete.")
    
    while True:
        # Play a game
        result = play_game()
        
        if result:
            wins += 1
        else:
            losses += 1
        
        # Display stats
        display_stats(wins, losses)
        
        # Play again?
        play_again = input("\nPlay again? (y/n): ").lower().strip()
        if play_again != 'y':
            print("\n" + "=" * 60)
            print("Thanks for playing Hangman!")
            print("=" * 60)
            display_stats(wins, losses)
            print("\nGoodbye! 👋")
            break


if __name__ == "__main__":
    main()