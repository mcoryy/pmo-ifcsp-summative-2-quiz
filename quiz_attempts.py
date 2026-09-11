import csv
from datetime import datetime

class QuizAttempts:
    def __init__(self, username):
        self.username = username
        self.score = 0
        self.attempts = 0

    def record_attempt(self, user_answer, expected_answer):
        cleaned_user = str(user_answer).strip().lower()
        cleaned_expected = str(expected_answer).strip().lower()

        print(f"INPUT -> User: '{cleaned_user}' | Expected: '{cleaned_expected}'")

        if cleaned_user == cleaned_expected:
            self.score += 1
            print("-> ✅ Correct! Score increased")
        else:
            print(f"-> ❌ Incorrect (Compared '{cleaned_user}' with '{cleaned_expected}')")
        
        self.attempts += 1

    def save_results(self, filename="quiz_results.csv"):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        try:
            with open(filename, mode="a", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow([self.username, self.score, timestamp])
            print("-> Results saved successfully to CSV!")
        except Exception as e:
            print(f"-> Error saving results: {e}")
