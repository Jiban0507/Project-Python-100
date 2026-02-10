# 📝 Flashcard Study App

A Python-based **flashcard study tool** to **create, store, and review flashcards**.
This system helps users **learn effectively**, **track study progress**, and **memorize content efficiently**.

---

## 🎯 Aim of the Project

To develop a **user-friendly flashcard application** where users can **add, save, and study flashcards**, making the learning process interactive and structured.

---

## 📝 Objectives

* Create flashcards with **question and answer pairs**.
* Store flashcards in a **persistent JSON file**.
* Review flashcards with **study mode** (show question → reveal answer).
* Navigate through flashcards sequentially.
* Provide a **simple GUI** using **Tkinter** for easy interaction.

---

## ✨ Features

* Add, view, and edit flashcards.
* Study flashcards with **question-answer toggle**.
* Persistent storage in **JSON file**.
* Cycle through flashcards with **Next Card** button.
* User-friendly **graphical interface**.

---

## ⚙️ Requirements

* Python 3.8+
* Libraries:

  * `tkinter` (built-in)
  * `json` (built-in)

No additional installations are required. Tkinter comes with Python.

---

## 📂 Project Structure

```
FlashcardApp/
│── flashcard_app.py      # Main Python program (GUI)
│── flashcards.json       # Persistent flashcard storage
│── README.md             # Project documentation
```

---

## 🚀 How to Run

1. Make sure you have Python installed (3.8+).
2. Run the program:

```bash
python flashcard_app.py
```

3. Use the GUI to:

   * Add Flashcards
   * Show Answer
   * Navigate Next Card

---

## 🧩 Code Overview

* **FlashcardApp** → Main class handling GUI, flashcard logic, and file storage.
* **load_flashcards()** → Loads flashcards from `flashcards.json`.
* **save_flashcards()** → Saves flashcards to JSON for persistence.
* **add_flashcard()** → Prompts user to add a question-answer pair.
* **show_answer()** → Toggles between question and answer.
* **next_card()** → Moves to the next flashcard.
* **update_card_display()** → Updates GUI to show the current card.

---

## 🗃️ Data Storage Structure

**File:** `flashcards.json`

Example content:

```json
[
    {
        "question": "What is Python?",
        "answer": "Python is a high-level programming language."
    },
    {
        "question": "What is Tkinter?",
        "answer": "Tkinter is a Python library for creating GUIs."
    }
]
```

---

## 🖥️ Sample Output (GUI)

**Main Window:**

```
--------------------------------------
| Flashcard Question/Answer Display  |
|                                    |
|       "What is Python?"            |
|                                    |
| [Show Answer]  [Next Card] [Add]  |
--------------------------------------
```

**User Flow Example:**

1. Click **Add Flashcard** → enter question & answer → saved automatically.
2. Click **Show Answer** → displays answer.
3. Click **Next Card** → moves to next flashcard.

---

## 🔮 Future Enhancements

* Shuffle flashcards for randomized study sessions.
* Track correct/incorrect answers for scoring.
* Categorize flashcards by subject or topic.
* Add search/filter options.
* Enhance GUI with color themes or progress bar.
* Export flashcards to CSV or other formats.

---

## 👤 Developer

**Name:** Jiban Maji
**GitHub:** [https://github.com/Jiban0507](https://github.com/Jiban0507)
