# Hangman Game 🎮 ![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=yellow)
![Python Logo](https://www.python.org/static/community_logos/python-logo.png)

A classic **Hangman Word Guessing Game** written in Python with ASCII art visualization.  
Guess the hidden word letter by letter before the hangman is complete!

---

## 📌 Features

- 🎯 **Three Difficulty Levels** - Easy, Medium, and Hard
- 🎨 **ASCII Art Hangman** - Visual representation of remaining tries
- 📊 **Game Statistics** - Track wins, losses, and win rate
- ✅ **Input Validation** - Prevents invalid guesses
- 🔄 **Replay Option** - Play multiple rounds in one session
- 📚 **Word Categories** - Curated word lists for each difficulty
- 🎲 **Random Selection** - Different word each game

---

## 🎮 How to Play

1. **Choose your difficulty level** (Easy/Medium/Hard)
2. **Guess letters** one at a time
3. **Correct guesses** reveal letters in the word
4. **Wrong guesses** add body parts to the hangman
5. **Win** by completing the word before 6 wrong guesses
6. **Lose** if the hangman drawing is completed

---

## 🎯 Difficulty Levels

### Easy 🟢
- **Word Length:** 3-4 letters
- **Examples:** cat, dog, sun, moon, tree
- **Perfect for:** Beginners and quick games

### Medium 🟡
- **Word Length:** 5-7 letters
- **Examples:** python, computer, keyboard, mountain
- **Perfect for:** Intermediate players

### Hard 🔴
- **Word Length:** 8+ letters
- **Examples:** algorithm, programming, technology
- **Perfect for:** Advanced players and challenge seekers

---

## 🚀 How to Run

### 1. Make sure you have Python 3 installed
Check using:
```bash
python --version
```
or
```bash
python3 --version
```

### 2. Run the program
```bash
python hangman.py
```
or
```bash
python3 hangman.py
```

### 3. Follow the Interactive Prompts
```
============================================================
           🎮 HANGMAN GAME 🎮
============================================================

Guess the word one letter at a time!
You have 6 tries before the hangman is complete.
```

---

## 📝 Gameplay Example

### Step 1: Select Difficulty
```
============================================================
SELECT DIFFICULTY LEVEL
============================================================
1. Easy   (3-4 letter words)
2. Medium (5-7 letter words)
3. Hard   (8+ letter words)
============================================================

Enter choice (1-3): 2
```

### Step 2: Game Begins
```
============================================================
🎮 GAME START!
============================================================
Difficulty: MEDIUM
Word length: 6 letters
You have 6 tries to guess the word!
```

### Step 3: Make Guesses
```
============================================================
       --------
       |      |
       |      
       |     
       |      
       |     
    -------
============================================================
Word: _ _ _ _ _ _

Tries remaining: 6
Wrong guesses: None
Guessed letters: 
============================================================

Guess a letter: p
✅ Correct! 'P' is in the word!
```

### Step 4: Continue Playing
```
============================================================
       --------
       |      |
       |      O
       |      |
       |      
       |     
    -------
============================================================
Word: p _ _ _ _ _

Tries remaining: 4
Wrong guesses: a, e
Guessed letters: a, e, p
============================================================

Guess a letter: y
✅ Correct! 'Y' is in the word!
```

### Step 5: Win or Lose
**Win:**
```
🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉
CONGRATULATIONS! You guessed the word: PYTHON
🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉
```

**Lose:**
```
       --------
       |      |
       |      O
       |     /|\
       |     / \
       |     
    -------

💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀
GAME OVER! The word was: COMPUTER
💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀
```

### Step 6: View Statistics
```
============================================================
📊 YOUR STATISTICS
============================================================
Games played: 5
Wins: 3
Losses: 2
Win rate: 60.0%
============================================================
```

---

## 📂 Folder Structure

```
Hangman-Game/
   ├── hangman.py       # Main Python script
   └── README.md        # Documentation
```

---

## 🎯 Game Rules

### Valid Guesses
- ✅ Single letters (a-z)
- ✅ One letter at a time
- ✅ Each letter can only be guessed once

### Invalid Guesses
- ❌ Numbers or special characters
- ❌ Multiple letters at once
- ❌ Previously guessed letters
- ❌ Empty input

### Lives System
- Start with **6 tries**
- Each wrong guess loses **1 try**
- Game ends when tries reach **0**
- Correct guesses don't consume tries

---

## 🎨 Hangman ASCII Stages

The hangman is drawn progressively with each wrong guess:

1. **Stage 0** - Empty gallows (6 tries left)
2. **Stage 1** - Head appears (5 tries left)
3. **Stage 2** - Body appears (4 tries left)
4. **Stage 3** - Left arm (3 tries left)
5. **Stage 4** - Right arm (2 tries left)
6. **Stage 5** - Left leg (1 try left)
7. **Stage 6** - Right leg - GAME OVER! (0 tries)

---

## 🎓 Learning Concepts

This project demonstrates:
- **Random Module** - Selecting random words
- **Sets** - Tracking guessed letters efficiently
- **String Manipulation** - Displaying hidden words
- **Control Flow** - Game loops and conditionals
- **Functions** - Modular code organization
- **ASCII Art** - Text-based graphics
- **Input Validation** - Ensuring valid user input
- **Statistics Tracking** - Recording game history

---

## 🛠️ Technologies Used

- **Python 3.x** - Programming language
- **random** - Random word selection
- **string** - Letter validation
- **ASCII Art** - Visual hangman display

---

## ✅ Purpose

- Practice Python fundamentals
- Learn game development basics
- Understand set operations
- Implement state management
- Create engaging user experiences
- Classic game for all ages!

---

## 🔮 Future Enhancements

- [ ] Add hint system (reveal a letter)
- [ ] Multiplayer mode (2-player)
- [ ] Custom word lists from files
- [ ] Timer mode for speed challenges
- [ ] Sound effects
- [ ] Color-coded terminal output
- [ ] Leaderboard system
- [ ] More word categories (animals, countries, movies)
- [ ] GUI version using Tkinter
- [ ] Online multiplayer

---

## 💡 Strategy Tips

1. **Start with vowels** (A, E, I, O, U) - they appear frequently
2. **Try common consonants** (T, N, S, R, L)
3. **Look for patterns** in revealed letters
4. **Consider word length** when guessing
5. **Think of common words** in the difficulty range
6. **Don't repeat guesses** - check guessed letters list

---

## 👨‍💻 Author

**Developed by Debanga**

---

## 📝 License

This project is open source and available for educational purposes.

---

## 🤝 Contributing

Want to add more words or features? Feel free to fork and submit a pull request!

### Adding New Words:
```python
WORD_LISTS = {
    "easy": ["your", "words", "here"],
    "medium": ["more", "words"],
    "hard": ["challenging", "vocabulary"]
}
```

---

**Have Fun Playing Hangman! 🎮✨**