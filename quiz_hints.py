import tkinter as tk

def create_hint_dropdown(parent, hint_text):
    hint_var = tk.StringVar(value="Need a hint?")
    hints_list = ["Need a hint?", hint_text if hint_text else "No hint available."]
    
    hint_actual = tk.OptionMenu(parent, hint_var, *hints_list)
    hint_actual.config(font=("Century Gothic", 14), fg="#ffffff", bg="#6c114c")
    hint_actual["menu"].config(font=("Century Gothic", 12), fg="#ffffff", bg="#6c114c")
    
    return hint_actual