import csv

def load_pmo_questions(filename="questions.csv"):
    questions = []
    with open(filename, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            questions.append(row)
    return questions