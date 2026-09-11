import tkinter as tk
from quiz_hints import create_hint_dropdown

BG = "#f4c1e6"
TEXT = "#660000"
BUTTON_TEXT = "#c13078"
FONT = ("Century Gothic", 18)

class QuizView(tk.Frame):
    def __init__(self, parent, question_data, submit_callback): 
        super().__init__(parent, bg=BG)
        self.submit_callback = submit_callback
        question_text = question_data.get("question")
        self.question_label = tk.Label(
            self, 
            text=question_text, 
            bg=BG, 
            fg=TEXT, 
            font=FONT, 
            wraplength=600
        )
        self.question_label.pack(pady=10)

        hint_text = question_data.get("hint", "")
        if hint_text:
            self.hint_dropdown = create_hint_dropdown(self, hint_text)
            self.hint_dropdown.pack(pady=5)

        options = [
            question_data.get("option_a"),
            question_data.get("option_b"),
            question_data.get("option_c"),
            question_data.get("option_d")
        ]
        options = [opt for opt in options if opt]

        self.var = tk.StringVar(value=options[0] if options else "")

        for option in options:
            rb = tk.Radiobutton(
                self,
                text=option,
                variable=self.var,
                value=option,
                bg=BG,
                fg=TEXT,
                font=("Century Gothic", 14),
                selectcolor=BG
            )
            rb.pack(anchor="w", padx=60, pady=4)

        self.button = tk.Button(
            self, 
            text="Submit Answer", 
            font=FONT, 
            fg=BUTTON_TEXT, 
            bg=BG, 
            command=self.validate_answer
        )
        self.button.pack(pady=20)

    def validate_answer(self):
        selected_option = self.var.get()
        print(f"QuizView captured choice: '{selected_option}'")
        self.submit_callback(selected_option)