import tkinter as tk
from tkinter import ttk
import random
import string

# Funktionen
def generate_password():
    length = length_var.get()
    charset = ""

    if use_uppercase.get():
        charset += string.ascii_uppercase
    if use_lowercase.get():
        charset += string.ascii_lowercase
    if use_numbers.get():
        charset += string.digits
    if use_specials.get():
        charset += string.punctuation

    if charset:
        password = "".join(random.choices(charset, k=length))
        generated_password.set(password)
    else:
        generated_password.set("Keine Optionen ausgewählt!")

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(generated_password.get())
    root.update_idletasks()

# Hauptfenster
root = tk.Tk()
root.title("Passwort-Generator")
root.geometry("400x300")
root.configure(padx=20, pady=20)

# Variablen initialisieren
length_var = tk.IntVar(value=8)
use_uppercase = tk.BooleanVar(value=True)
use_lowercase = tk.BooleanVar(value=True)
use_numbers = tk.BooleanVar(value=True)
use_specials = tk.BooleanVar(value=False)
generated_password = tk.StringVar(value="")

# Widgets erstellen
# Passwortlänge
ttk.Label(root, text="Passwortlänge:").grid(row=0, column=0, sticky="w", pady=5)
ttk.Entry(root, textvariable=length_var, width=5).grid(row=0, column=1, sticky="w")

# Optionen
ttk.Checkbutton(root, text="Großbuchstaben (A-Z)", variable=use_uppercase).grid(row=1, column=0, sticky="w")
ttk.Checkbutton(root, text="Kleinbuchstaben (a-z)", variable=use_lowercase).grid(row=2, column=0, sticky="w")
ttk.Checkbutton(root, text="Zahlen (0-9)", variable=use_numbers).grid(row=3, column=0, sticky="w")
ttk.Checkbutton(root, text="Sonderzeichen (!@#$)", variable=use_specials).grid(row=4, column=0, sticky="w")

# Generieren-Button
ttk.Button(root, text="Generiere Passwort", command=generate_password).grid(row=5, column=0, pady=10, columnspan=2)

# Ausgabe
ttk.Label(root, text="Generiertes Passwort:").grid(row=6, column=0, sticky="w")
ttk.Entry(root, textvariable=generated_password, state="readonly", width=40).grid(row=7, column=0, columnspan=2, pady=5)

# Kopieren-Button
ttk.Button(root, text="Kopieren", command=copy_to_clipboard).grid(row=8, column=0, columnspan=2, pady=10)

# Hauptloop starten
root.mainloop()