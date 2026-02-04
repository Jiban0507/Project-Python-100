from tkinter import Tk, filedialog, Button, Label, Listbox, END
from PyPDF2 import PdfMerger


def select_files():
    global pdf_files
    files = filedialog.askopenfilenames(title="Select PDF Files", filetypes=[("PDF Files", "*.pdf")])
    if files:
        pdf_files = list(files)
        listbox.delete(0, END)
        for f in pdf_files:
            listbox.insert(END, f.split("/")[-1])
        status_label.config(text=f"{len(pdf_files)} file(s) selected")
    else:
        status_label.config(text="No files selected")


def merge_pdfs():
    if not pdf_files:
        status_label.config(text="No files selected!")
        return
    merger = PdfMerger()
    for pdf in pdf_files:
        merger.append(pdf)
    save_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
    if save_path:
        merger.write(save_path)
        merger.close()
        status_label.config(text=f"Merged PDF saved at:\n{save_path}")
        listbox.delete(0, END)
        pdf_files.clear()
    else:
        status_label.config(text="Merge cancelled")


def clear_selection():
    pdf_files.clear()
    listbox.delete(0, END)
    status_label.config(text="Selection cleared")


root = Tk()
root.title("PDF Merger")
root.geometry("500x400")
root.resizable(False, False)


pdf_files = []


select_button = Button(root, text="Select PDFs", width=20, command=select_files)
select_button.pack(pady=10)


clear_button = Button(root, text="Clear Selection", width=20, command=clear_selection)
clear_button.pack(pady=5)


merge_button = Button(root, text="Merge PDFs", width=20, command=merge_pdfs)
merge_button.pack(pady=5)


listbox = Listbox(root, width=60, height=10)
listbox.pack(pady=10)


status_label = Label(root, text="Select PDF files to merge", wraplength=450)
status_label.pack(pady=10)


root.mainloop()