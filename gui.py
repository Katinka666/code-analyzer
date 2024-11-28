import tkinter as tk
from tkinter import ttk
import route
import logging

# logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# create window
root = tk.Tk()
root.title("Code Analyzer")
root.geometry("600x600")

# info label
info_label = ttk.Label(root, text="Másold be a kódot az alábbi mezőbe:")
info_label.pack(pady=10)

# code box
code_box = tk.Text(root, wrap="word", height=15, width=70)
code_box.pack(padx=10, pady=10, expand=True, fill="both")

# scrollbar
scrollbar = ttk.Scrollbar(root, command=code_box.yview)
code_box.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")

# analysis type (defined by the radio buttons)
selected_option = tk.StringVar(value="Hibakeresés")  # default value
user_code = ""

# radio buttons
radio_error = tk.Radiobutton(root, text="Hibakeresés", value="Hibakeresés", variable=selected_option)
radio_error.pack(anchor="w")
radio_opt = tk.Radiobutton(root, text="Optimalizálás", value="Optimalizálás", variable=selected_option)
radio_opt.pack(anchor="w")
radio_sec = tk.Radiobutton(root, text="Biztonsági elemzés", value="Biztonsági elemzés", variable=selected_option)
radio_sec.pack(anchor="w")

# handling the button click event
def analyze_button_click():
    user_code = code_box.get("1.0", tk.END)
    # destroying widgets
    radio_error.destroy()
    radio_opt.destroy()
    radio_sec.destroy()
    code_box.destroy()
    analyze_button.destroy()
    info_label.destroy()

    # response
    logging.info("Getting response started...")
    response = route.get_response(selected_option.get(), user_code)

    # response label
    response_label = ttk.Label(root, text=response, wraplength=500)
    response_label.pack(pady=10)


analyze_button = ttk.Button(root, text="Mehet", command=analyze_button_click)
analyze_button.pack(pady=10)

root.mainloop()