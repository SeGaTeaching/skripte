import requests
import tkinter as tk
from tkinter import ttk, messagebox

# Globale Variablen
api_key = "55d50301c8add778a9ca4369"
url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"

def get_currencies():
    response = requests.get(f"https://v6.exchangerate-api.com/v6/{api_key}/codes")
    data = response.json()
    currencies = data["supported_codes"]
    return {f'{abbr} - {name}': abbr for abbr, name in currencies}

abbriviation_currencies_dict = get_currencies()

def get_exchange_rate(from_value_abbr, to_value_abbr):
    try:
        response = requests.get(url+from_value_abbr)
        data = response.json()
        if data["result"] != "error" and data["conversion_rates"][to_value_abbr]:
            return data["conversion_rates"][to_value_abbr]
        else:
            messagebox.showwarning("Fehler", "Diese Währung wird nicht unterstützt")
    except:
        messagebox.showwarning("Anfrage Fehler", "Deine Anfrage konnte nicht verarbeitet werden")

def convert_currency():
    try:
        amount = float(amount_entry.get())
        from_value = from_box.get()
        to_value = to_box.get()
        from_value_abbr = abbriviation_currencies_dict[from_value]
        to_value_abbr = abbriviation_currencies_dict[to_value]
        rate = get_exchange_rate(from_value_abbr, to_value_abbr)
        result = amount * rate
        result_label.configure(text=f'{result:.2f} {to_value}', font=("Arial", 15), fg="green")
        messagebox.showinfo("Erfolg", f"{amount} {from_value} sind {result:.2f} {to_value}")
    except ValueError:
        messagebox.showerror("Eingabefehler", "Bitte eine Zahl als Nummer eingeben")

root = tk.Tk()
root.title("Währungsumrechner")
root.geometry("800x160")
root.resizable(False, False)

frame = tk.Frame(root)
frame.pack(fill="both", expand=True, pady=15, padx=15)

amount_label = tk.Label(frame, text="Betrag", font=("Arial", 14))
amount_entry = tk.Entry(frame, font=("Arial", 14))

from_label = tk.Label(frame, text="Von", font=("Arial", 14))
from_box = ttk.Combobox(frame, state="readonly", font=("Arial", 14), values=list(abbriviation_currencies_dict.keys()))
from_box.set("EUR - Euro")

to_label = tk.Label(frame, text="in", font=("Arial", 14))
to_box = ttk.Combobox(frame, state="readonly", font=("Arial", 14), values=list(abbriviation_currencies_dict.keys()))
to_box.set("USD - United States Dollar")

# Layout
amount_label.grid(row=0, column=0, sticky="w")
amount_entry.grid(row=1, column=0, sticky="we")
from_label.grid(row=0, column=1, sticky="w")
from_box.grid(row=1, column=1, sticky="we")
to_label.grid(row=0, column=2, sticky="w")
to_box.grid(row=1, column=2, sticky="we")

result_label = tk.Label(frame, text="Ergebnis...", font=("Arial", 12))
result_label.grid(row=2, column=0, sticky="w", columnspan=2, pady=(20,10))

ttk.Button(frame, text="Umrechnen", command=convert_currency).grid(row=2, column=2, sticky="ew", pady=(20,10))

frame.columnconfigure((0,1,2), weight=1)

root.mainloop()