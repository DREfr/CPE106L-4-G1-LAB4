import tkinter as tk
from tkinter import filedialog, Text

def open_file():
    file_path = filedialog.askopenfilename(
        title="Select a text file",
        filetypes=[("Text files", "*.txt")]
    )
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
        text_widget.delete(1.0, tk.END)
        text_widget.insert(tk.END, content)

root = tk.Tk()
root.title("File Dialog Example")
root.geometry("600x400")

open_file_button = tk.Button(root, text="Open File", command=open_file, font=("Arial", 14))
open_file_button.pack(pady=20)

text_widget = Text(root, wrap=tk.WORD, font=("Arial", 12))
text_widget.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

root.mainloop()
