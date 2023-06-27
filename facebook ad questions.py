import tkinter as tk
from tkinter import filedialog
import os

def select_file():
    global selected_file
    selected_file = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if selected_file:
        select_button.config(state=tk.DISABLED, text="✅ File Selected")

def copy_to_clipboard(question, button):
    if selected_file:
        with open(selected_file, 'r') as file:
            content = file.read()

        modified_content = f"Can you tell me if this copy complies with Facebook's {question} policy?\n((( {content} )))"
        root.clipboard_clear()
        root.clipboard_append(modified_content)
        button.config(text="✅ Copied", state=tk.DISABLED)

root = tk.Tk()
root.title("Text File Processor")

# Left column - Instructions and app description
instructions_label = tk.Label(root, text="Instructions:\n\n1. Click the 'Select File' button to choose a text file.\n2. Choose a question category.\n3. The modified content will be copied to the clipboard.")
instructions_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)

# Right column - File selection and question buttons
select_button = tk.Button(root, text="Select File", command=select_file)
select_button.grid(row=0, column=1, padx=10, pady=10)

questions = [
    "Prohibited Content",
    "Community Standards",
    "Misleading Claims",
    "Personal Attributes",
    "Discrimination",
    "Sensational or Shocking Content",
    "Trademarks and Copyrights",
    "Data Collection and Privacy",
    "Restricted Content",
    "Landing Page Compliance"
]

buttons = {}
for i, question in enumerate(questions, start=1):
    button = tk.Button(root, text=question, command=lambda q=question: copy_to_clipboard(q, buttons[q]))
    button.grid(row=i, column=1, padx=10, pady=5, sticky="w")
    buttons[question] = button

root.mainloop()
