import tkinter as tk
from tkinter import messagebox
import time

# ---------------------------- CONSTANTS ------------------------------- #
WORK_MIN = 25        # Work duration
SHORT_BREAK_MIN = 5  # Short break
LONG_BREAK_MIN = 15  # Long break
REPS = 0             # Pomodoro counter
timer = None         # To store after() id
timer_running = False  # To prevent multiple starts

# ---------------------------- TIMER RESET ---------------------------- #
def reset_timer():
    global REPS, timer, timer_running
    if timer:
        window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer", fg="green")
    session_label.config(text="")
    REPS = 0
    timer_running = False
    check_marks.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------- #
def start_timer():
    global REPS, timer_running
    if timer_running:
        return  # Prevent multiple timers
    timer_running = True

    # Show session summary notice
    notice = (
        "Pomodoro Steps:\n"
        "1. Work 25 min\n"
        "2. Short Break 5 min\n"
        "3. Work 25 min\n"
        "4. Short Break 5 min\n"
        "5. Work 25 min\n"
        "6. Short Break 5 min\n"
        "7. Work 25 min\n"
        "8. Long Break 15–30 min\n\n"
        "Click OK to start."
    )
    messagebox.showinfo("Pomodoro Timer Steps", notice)

    start_next_session()

def start_next_session():
    global REPS
    REPS += 1

    if REPS % 8 == 0:
        count = LONG_BREAK_MIN * 60
        label.config(text="Long Break", fg="red")
    elif REPS % 2 == 0:
        count = SHORT_BREAK_MIN * 60
        label.config(text="Short Break", fg="pink")
    else:
        count = WORK_MIN * 60
        label.config(text="Work", fg="green")

    session_label.config(text=f"Session {REPS}/8")
    count_down(count)

# ---------------------------- COUNTDOWN MECHANISM -------------------- #
def count_down(count):
    global timer, timer_running
    minutes = count // 60
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        # Show notification
        if REPS % 2 == 1:
            messagebox.showinfo("Time's up!", "Work session over! Take a break.")
        else:
            messagebox.showinfo("Time's up!", "Break over! Time to work.")
        # Update check marks
        marks = "✔" * ((REPS + 1)//2)
        check_marks.config(text=marks)
        timer_running = False
        start_next_session()  # Automatically start next session

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg="#f7f5dd")

# Timer label
label = tk.Label(text="Timer", fg="green", bg="#f7f5dd", font=("Courier", 35, "bold"))
label.grid(column=1, row=0)

# Session info
session_label = tk.Label(fg="black", bg="#f7f5dd", font=("Courier", 15, "bold"))
session_label.grid(column=1, row=1)

# Canvas for timer text
canvas = tk.Canvas(width=200, height=224, bg="#f7f5dd", highlightthickness=0)
timer_text = canvas.create_text(100, 112, text="00:00", fill="black", font=("Courier", 35, "bold"))
canvas.grid(column=1, row=2)

# Start button
start_button = tk.Button(text="Start", command=start_timer)
start_button.grid(column=0, row=3)

# Reset button
reset_button = tk.Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=3)

# Check marks for completed work sessions
check_marks = tk.Label(fg="green", bg="#f7f5dd", font=("Courier", 20, "bold"))
check_marks.grid(column=1, row=4)

window.mainloop()
