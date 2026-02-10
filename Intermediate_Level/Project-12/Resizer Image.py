import os
from tkinter import *
from tkinter import filedialog, messagebox, ttk
from PIL import Image

input_files = []

def select_images():
    files = filedialog.askopenfilenames(
        title="Select Images",
        filetypes=[("Image Files", "*.jpg *.jpeg *.png")]
    )
    if files:
        input_files.clear()
        input_files.extend(files)
        selected_label.config(text=f"{len(input_files)} images selected")

def resize_images():
    if not input_files:
        messagebox.showerror("Error", "Please select images first")
        return

    out = filedialog.askdirectory(title="Select Output Folder")
    if not out:
        return

    try:
        if resize_mode.get() == 1:
            w = int(width_entry.get())
            h = int(height_entry.get())
        else:
            percent = int(percent_entry.get())
    except:
        messagebox.showerror("Error", "Please enter valid numbers")
        return

    progress["maximum"] = len(input_files)
    progress["value"] = 0

    count = 0

    for img_path in input_files:
        try:
            img = Image.open(img_path)

            if resize_mode.get() == 1:
                img.thumbnail((w, h), Image.LANCZOS)
            else:
                new_w = int(img.width * percent / 100)
                new_h = int(img.height * percent / 100)
                img = img.resize((new_w, new_h), Image.LANCZOS)

            name = os.path.basename(img_path)
            img.save(os.path.join(out, name))

            count += 1
            progress["value"] += 1
            root.update_idletasks()

        except:
            pass

    messagebox.showinfo("Success", f"{count} images resized successfully!")

root = Tk()
root.title("Image Resizer Tool")
root.geometry("460x480")
root.resizable(False, False)

resize_mode = IntVar(value=1)

Label(root, text="IMAGE RESIZER TOOL", font=("Arial", 16, "bold")).pack(pady=10)

Button(root, text="Select Images (Gallery)", command=select_images).pack()
selected_label = Label(root, text="No images selected")
selected_label.pack(pady=5)

Label(root, text="Resize Mode", font=("Arial", 12, "bold")).pack(pady=10)

Radiobutton(root, text="Width & Height", variable=resize_mode, value=1).pack()
frame1 = Frame(root)
frame1.pack(pady=5)

Label(frame1, text="Max Width").grid(row=0, column=0)
width_entry = Entry(frame1, width=10)
width_entry.grid(row=0, column=1, padx=5)

Label(frame1, text="Max Height").grid(row=0, column=2)
height_entry = Entry(frame1, width=10)
height_entry.grid(row=0, column=3, padx=5)

Radiobutton(root, text="Percentage Based", variable=resize_mode, value=2).pack(pady=5)
frame2 = Frame(root)
frame2.pack()

Label(frame2, text="Percentage (%)").grid(row=0, column=0)
percent_entry = Entry(frame2, width=10)
percent_entry.grid(row=0, column=1, padx=5)

progress = ttk.Progressbar(root, length=350)
progress.pack(pady=20)

Button(
    root,
    text="Resize Images",
    bg="green",
    fg="white",
    font=("Arial", 12),
    command=resize_images
).pack(pady=10)

root.mainloop()