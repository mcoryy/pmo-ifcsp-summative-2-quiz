import tkinter as tk 
from load_questions import load_pmo_questions 
from quiz_names import clean_name, presence_check, length_check, character_check
from quiz_attempts import QuizAttempts
from quiz_questions import QuizView

BG = "#f4c1e6"
TEXT = "#660000"
BUTTON_TEXT = "#c13078"

class QuizApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Project Management Quiz")
        self.geometry("1000x750")
        self.config(bg=BG)
        self.questions = load_pmo_questions()
        self.username = ""
        self.attempts = None
        self.name_var = tk.StringVar()
        self.error_label = None
        self.show_opening_screen()

    def clear_window(self):
        for widget in self.winfo_children():
            widget.destroy()

    def show_opening_screen(self):
        self.clear_window()
        
        frame = tk.Frame(self, bg=BG)
        frame.pack(expand=True)

        tk.Label(
            frame,
            text="Welcome to the Project Management Quiz!",
            bg=BG,
            fg=TEXT,
            font=("Century Gothic", 20)
        ).pack(pady=10)

        tk.Label(
            frame,
            text="This quiz can help you understand how well your skills would fit into the Project Management office. \n\n Please enter your name in the box below:",
            bg=BG,
            fg=TEXT,
            font=("Century Gothic", 18)
        ).pack(pady=10)

        entry = tk.Entry(
            frame,
            textvariable=self.name_var,
            font=("Century Gothic", 18),
            fg="#ffffff"
        )
        entry.pack(pady=10)

        self.error_label = tk.Label(frame, text="", bg=BG, fg="red", font=("Century Gothic", 14))
        self.error_label.pack(pady=5)

        tk.Button(
            frame,
            text="Start Quiz",
            font=("Century Gothic", 18),
            fg=BUTTON_TEXT,
            bg=BG,
            command=self.validate_and_start
        ).pack(pady=10)

    def validate_and_start(self):
        raw_name = self.name_var.get()
        
        errors = []
        if not presence_check(raw_name):
            errors.append("Name cannot be empty!")
        elif not length_check(raw_name):
            errors.append("Name must be between 2 and 50 characters long!")
        elif not character_check(raw_name):
            errors.append("Name cannot contain numbers or special characters like '!, ?, &'!")
        if errors:
            self.error_label.config(text="\n".join(errors))
            return
        
        self.username = clean_name(raw_name)
        self.attempts = QuizAttempts(self.username)
        self.show_question()

    def show_question(self):
        self.clear_window()
        idx = self.attempts.attempts if self.attempts else 0
        
        if idx < len(self.questions):
            q_data = self.questions[idx]
            self.q_view = QuizView(self, q_data, self.handle_answer)
            self.q_view.pack(expand=True)
        else:
            self.finish_quiz()

    def handle_answer(self, user_answer):
        idx = self.attempts.attempts
        q_data = self.questions[idx]
        ans_key = q_data.get("answer", "").strip().lower()
        expected = q_data.get(ans_key, "")

        self.attempts.record_attempt(user_answer, expected)
        self.show_question()

    def finish_quiz(self):
        print("-> finish_quiz() has been triggered!")

        if self.attempts:
            self.attempts.save_results()

        self.clear_window()
        total_q = len(self.questions) if self.questions else 0
        final_score = self.attempts.score if self.attempts else 0
        display_name = self.username if self.username else "User"
        score_label = tk.Label(
            self, 
            text=f"Well Done {display_name}!\n\nYou scored: {final_score} / {total_q}", 
            font=("Century Gothic", 18),
            bg=BG,
            fg=TEXT
        )
        score_label.pack(expand=True, pady=20)

        tk.Button(
            self,
            text="QUIT",
            font=("Century Gothic", 18),
            fg=BUTTON_TEXT,
            bg=BG,
            command=self.destroy
        ).pack(pady=20)

if __name__ == "__main__":
    app = QuizApp()
    app.mainloop()