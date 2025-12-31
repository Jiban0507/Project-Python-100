# Beginner Level

import random

def hangman():
    words = ['python', 'hangman', 'programming', 'developer', 'code']
    word = random.choice(words)
    guessed = '_' * len(word)
    guessed_list = list(guessed)
    tries = 6
    guessed_letters = []

    print("Welcome to Hangman!")
    
    while tries > 0 and '_' in guessed_list:
        print('Current word: ' + ' '.join(guessed_list))
        print(f'You have {tries} tries left.')
        guess = input('Guess a letter: ').lower()

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            for index, letter in enumerate(word):
                if letter == guess:
                    guessed_list[index] = guess
            print("Good guess!")
        else:
            tries -= 1
            print("Wrong guess!")

    if '_' not in guessed_list:
        print(f'Congratulations! You guessed the word: {word}')
    else:
        print(f'Sorry, you ran out of tries. The word was: {word}')

hangman()
