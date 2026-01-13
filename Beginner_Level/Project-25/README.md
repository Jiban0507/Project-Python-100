# ⌨️ Typing Speed Test Application

A Python-based command-line typing speed test application that measures your typing speed (WPM) and accuracy. Practice your typing skills with three difficulty levels and get instant feedback with color-coded results.

## ✨ Features

- 🎯 **Three Difficulty Levels**: Easy, Medium, and Hard
- ⚡ **Real-time Speed Calculation**: Measures Words Per Minute (WPM)
- 📊 **Accuracy Tracking**: Calculates typing accuracy percentage
- 🎨 **Color-coded Feedback**: 
  - 🟢 Green for correctly typed words
  - 🔴 Red for incorrectly typed words
  - 🟡 Yellow highlight for the reference text
- ⏱️ **Countdown Timer**: 3-second countdown before starting
- 📝 **Detailed Results**: Shows time taken, WPM, accuracy, and wrong words
- 🎲 **Random Sentences**: Different sentence for each test attempt

## 📋 Requirements

- Python 3.6 or higher
- No external dependencies required (uses only built-in Python libraries)

## 🚀 Installation

1. Clone or download this repository
2. Navigate to the project directory:
   ```bash
   cd Project-25
   ```

## 💻 Usage

### Running the Application

Simply run the Python script:

```bash
python Typing.py
```

### How to Use

1. **Choose Difficulty Level**: 
   - Enter `easy`, `medium`, or `hard` when prompted
   - If an invalid choice is entered, it defaults to `medium`

2. **Read the Text**: 
   - A highlighted sentence will be displayed
   - Read it carefully before starting

3. **Start Typing**: 
   - Press Enter when ready
   - A 3-second countdown will begin
   - Start typing the sentence when you see "Go!"

4. **View Results**: 
   - After typing, press Enter to see your results
   - Results include:
     - Time taken
     - Words per minute (WPM)
     - Accuracy percentage
     - Color-coded typed text
     - List of wrong words (if any)

## 📊 Difficulty Levels

### Easy
Short, simple sentences perfect for beginners:
- "Python is fun."
- "Typing is easy."
- "Practice daily."

### Medium
Moderate-length sentences with common words:
- "Python is a powerful programming language used for web development and data science."
- "Typing speed tests help improve accuracy and efficiency in everyday computer use."
- "Practice makes perfect when learning coding and typing together."

### Hard
Longer, more complex sentences with advanced vocabulary:
- "Libraries and functions in Python allow developers to build complex applications with efficiency and clarity."
- "Typing speed and accuracy are essential skills for programmers, writers, and students in the digital age."
- "Consistent practice with challenging paragraphs improves both cognitive focus and muscle memory in typing."

## 📈 Understanding Results

### Words Per Minute (WPM)
- Calculated as: `(Number of words typed / Time in seconds) × 60`
- Average typing speeds:
  - Beginner: 20-30 WPM
  - Intermediate: 40-50 WPM
  - Advanced: 60+ WPM
  - Professional: 80+ WPM

### Accuracy
- Calculated as: `(Correct words / Total words) × 100`
- Aim for 95%+ accuracy for good typing skills

### Color Coding
- **Green words**: Correctly typed
- **Red words**: Incorrectly typed
- Review red words to identify common mistakes

## 🎯 Example Output

```
Choose difficulty level: easy / medium / hard
Enter level: medium

Type the following paragraph as fast and accurately as you can:

Python is a powerful programming language used for web development and data science.

Press Enter when you are ready to start...

Starting in 3...
Go!

Start typing here:
Python is a powerful programming language used for web development and data science.

--- Results ---
Time taken: 0 minute 8 second
Words per minute (WPM): 45.00
Accuracy: 100.00%

Your typing with highlights:
Python is a powerful programming language used for web development and data science.

No mistakes! Well done 🎉
```

## 🔧 How It Works

1. **Sentence Selection**: Randomly selects a sentence from the chosen difficulty level
2. **Timer**: Records start and end time when you begin and finish typing
3. **Word Comparison**: Compares each word you typed with the reference text
4. **Calculations**:
   - WPM: Calculates words per minute based on time taken
   - Accuracy: Compares correct words vs total words
5. **Visual Feedback**: Uses ANSI color codes to highlight correct/incorrect words

## 📁 Project Structure

```
Project-25/
├── Typing.py      # Main application file
└── README.md      # This file
```

## 🎨 Code Features

- **Modular Design**: Functions for calculation, formatting, and display
- **Error Handling**: Defaults to medium level for invalid input
- **Color Support**: Uses ANSI escape codes for terminal colors
- **User-Friendly**: Clear prompts and formatted output

## 🚀 Future Enhancements

Potential improvements you could add:

- [ ] Save results to a file for tracking progress over time
- [ ] Add more sentences to each difficulty level
- [ ] Implement a leaderboard system
- [ ] Add character-level accuracy (not just word-level)
- [ ] Create a GUI version using tkinter or PyQt
- [ ] Add different test modes (1-minute test, 5-minute test)
- [ ] Track typing statistics and show improvement graphs
- [ ] Add custom sentence input option
- [ ] Implement typing practice mode with hints

## 🐛 Troubleshooting

### Colors Not Showing
- The application uses ANSI color codes that work in most modern terminals
- If colors don't appear, your terminal may not support ANSI codes
- The application will still function, just without color highlighting

### Windows Terminal
- Works best in PowerShell, Command Prompt, or Windows Terminal
- For best experience, use Windows Terminal or VS Code integrated terminal

## 📝 Notes

- The timer starts when you begin typing and stops when you press Enter
- Make sure to type exactly as shown (including punctuation and capitalization)
- Spaces between words are important for accurate word counting
- The application compares word-by-word, not character-by-character

## 🤝 Contributing

Feel free to:
- Add more sentences to each difficulty level
- Improve the accuracy calculation
- Add new features
- Report bugs or suggest improvements

## 📄 License

This project is open source and available for educational purposes.

## 👨‍💻 Author

Part of the Python 100 Projects series - Beginner Level

---

**Happy Typing! 🎉**

Improve your typing speed and accuracy with regular practice!
