import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

# File to store flashcards (always in the same folder as this script)
DATA_FILE = os.path.join(os.path.dirname(__file__), "flashcards.json")

class FlashcardApp:
    def __init__(self, master):
        self.master = master
        master.title("Flashcard Study App")
        master.geometry("400x300")

        # Load flashcards from JSON
        self.flashcards = self.load_flashcards()
        self.index = 0
        self.showing_answer = False

        # GUI Elements
        self.question_label = tk.Label(master, text="", font=("Arial", 16), wraplength=350)
        self.question_label.pack(pady=30)

        self.show_button = tk.Button(master, text="Show Answer", command=self.show_answer)
        self.show_button.pack(pady=5)

        self.next_button = tk.Button(master, text="Next Card", command=self.next_card)
        self.next_button.pack(pady=5)

        self.add_button = tk.Button(master, text="Add Flashcard", command=self.add_flashcard)
        self.add_button.pack(pady=5)

        # Display the first card (if any)
        self.update_card_display()

    def load_flashcards(self):
        """Load flashcards from JSON file."""
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                try:
                    data = json.load(f)
                    if isinstance(data, list):
                        return data
                except json.JSONDecodeError:
                    pass
        return []  # Return empty list if file doesn't exist or is invalid

    def save_flashcards(self):
        """Save all flashcards to JSON file."""
        with open(DATA_FILE, "w") as f:
            json.dump(self.flashcards, f, indent=4)

    def update_card_display(self):
        """Update the displayed card."""
        if not self.flashcards:
            self.question_label.config(text="No flashcards available.\nAdd one!")
            self.show_button.config(state="disabled")
            self.next_button.config(state="disabled")
        else:
            card = self.flashcards[self.index]
            self.question_label.config(text=card["question"])
            self.show_button.config(state="normal", text="Show Answer")
            self.next_button.config(state="normal")
            self.showing_answer = False

    def show_answer(self):
        """Toggle between question and answer."""
        if not self.flashcards:
            return
        card = self.flashcards[self.index]
        if not self.showing_answer:
            self.question_label.config(text=card["answer"])
            self.show_button.config(text="Hide Answer")
            self.showing_answer = True
        else:
            self.question_label.config(text=card["question"])
            self.show_button.config(text="Show Answer")
            self.showing_answer = False

    def next_card(self):
        """Move to the next flashcard."""
        if not self.flashcards:
            return
        self.index = (self.index + 1) % len(self.flashcards)
        self.update_card_display()

    def add_flashcard(self):
        """Add a new flashcard."""
        question = simpledialog.askstring("Add Flashcard", "Enter the question:")
        if not question:
            return
        answer = simpledialog.askstring("Add Flashcard", "Enter the answer:")
        if not answer:
            return

        # Append new card to the existing list
        self.flashcards.append({"question": question, "answer": answer})
        self.save_flashcards()  # Save all cards including previous ones
        self.index = len(self.flashcards) - 1  # Show the newly added card
        self.update_card_display()
        messagebox.showinfo("Saved", "Flashcard added successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()
