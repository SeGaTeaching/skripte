import tkinter as tk
from tkinter import ttk
import random
import string

class PasswordGeneratorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Passwort-Generator")
        self.geometry("400x300")
        self.configure(padx=20, pady=20)

        # Variablen initialisieren
        self.length_var = tk.IntVar(value=8)
        self.use_uppercase = tk.BooleanVar(value=True)
        self.use_lowercase = tk.BooleanVar(value=True)
        self.use_numbers = tk.BooleanVar(value=True)
        self.use_specials = tk.BooleanVar(value=False)
        self.generated_password = tk.StringVar(value="")

        # Widgets hinzufügen
        self._create_widgets()

    def _create_widgets(self):
        # Passwortlänge
        ttk.Label(self, text="Passwortlänge:").grid(row=0, column=0, sticky="w", pady=5)
        ttk.Entry(self, textvariable=self.length_var, width=5).grid(row=0, column=1, sticky="w")

        # Optionen
        ttk.Checkbutton(self, text="Großbuchstaben (A-Z)", variable=self.use_uppercase).grid(row=1, column=0, sticky="w")
        ttk.Checkbutton(self, text="Kleinbuchstaben (a-z)", variable=self.use_lowercase).grid(row=2, column=0, sticky="w")
        ttk.Checkbutton(self, text="Zahlen (0-9)", variable=self.use_numbers).grid(row=3, column=0, sticky="w")
        ttk.Checkbutton(self, text="Sonderzeichen (!@#$)", variable=self.use_specials).grid(row=4, column=0, sticky="w")

        # Generieren-Button
        ttk.Button(self, text="Generiere Passwort", command=self.generate_password).grid(row=5, column=0, pady=10, columnspan=2)

        # Ausgabe
        ttk.Label(self, text="Generiertes Passwort:").grid(row=6, column=0, sticky="w")
        ttk.Entry(self, textvariable=self.generated_password, state="readonly", width=40).grid(row=7, column=0, columnspan=2, pady=5)

        # Kopieren-Button
        ttk.Button(self, text="Kopieren", command=self.copy_to_clipboard).grid(row=8, column=0, columnspan=2, pady=10)

    def generate_password(self):
        length = self.length_var.get()
        charset = ""

        if self.use_uppercase.get():
            charset += string.ascii_uppercase
        if self.use_lowercase.get():
            charset += string.ascii_lowercase
        if self.use_numbers.get():
            charset += string.digits
        if self.use_specials.get():
            charset += string.punctuation

        if charset:
            password = "".join(random.choices(charset, k=length))
            self.generated_password.set(password)
        else:
            self.generated_password.set("Keine Optionen ausgewählt!")

    def copy_to_clipboard(self):
        self.clipboard_clear()
        self.clipboard_append(self.generated_password.get())
        self.update_idletasks()

if __name__ == "__main__":
    app = PasswordGeneratorApp()
    app.mainloop()