# ifcs-summative-2

## Introduction
The Project Management Quiz Application is a minimum viable product (MVP) developed to support onboarding and employee alignment for the Project Management office (PMO).

Working in the modern Project Manangement office involves strong decision making, documentation management and adherence to Governance and Compliance protocals, including handling of OFFICIAL-SENSITIVE documents. This application serves as an interactive tool to evaluate whether incoming personnel have the baseline knowledge to fulfil a Project Management role successfully. 

This is an important application for four key reasons:
1. It acts as a standard baseline assessment, targeting ten basic multiple choice questions. It establishes a reliable baseline for each candidate, testing their understanding of the role and environment as a whole, bridging the gap between theoretical knowledge and practical decision making.
2. This assessment can help align new employees into a role. Not everybody is suited to technology, admin or consulting. This quiz can help users and hiring staff identify where an induvidual excels and this quiz can specifically position users to the project management office, ensuring each employee is placed where they can add the maximum value.
3. Some question's test user's governance and compliance skills. Project Manager's  frequently deal with sensitive information and documentation. Incorporating OFFICIAL-SENSITIVE docments, the quiz ensures new personnel recognise the importance of regulatory standards, security and governance protocols before actually dealing with real-world data.
4. This application allows hiring staff to see real, objective metrics. Automatically saving scores, timestamps and name's. These are filtered through to a CSV file where data can be extracted into easily understood tables, improving role alignment strategies.

This quiz can be used as a filter during onboarding to save time, align roles and match employee's to their natural strengths. Overall helping to improve the flow of a PMO that handle's regular and sensitive data.

Some of the key technology used to create this includes [Python](https://docs.python.org/3/) and [Tkinter](https://docs.python.org/3/library/tkinter.html).

## Design
**GUI Design**

***Figure 1*** shows a wireframe design made on Figma during the early design of the quiz.
This design shows the user journey of the quiz, from entering a valid name to answering questions, reading hints, submitting the final answers and reaching the end score screen.

This wireframe was used to plan the colour schemes, screen layout and navigation flow before implementation. It focuses on all key elements of the quiz including colour scheme, structure, flow, user interaction and the sequence of questions.

![Figure 1: Wireframe Design (My own design made using Figma)](docs_assets/wireframe.png)

**Figure 1:** Wireframe Design (My own design made using Figma)

### Functional and Non-Functional Requirements
**Functional Requirements**

| ID  | Requirements |
|-----|--------------|
| FR1 | The application must allow a participant to enter their name. |
| FR2 | The application must prevent names with special characters, numerical digits. |
| FR3 | The application mustn't allow blank names to be submitted, there has to be a minimum of 2 characters. |
| FR4 | The application must load 10 multiple choice questions, one after the other. |
| FR5 | Each question must present a realistic Project Management scenario. |
| FR6 | At least one question must test the user's knowledge of SENSITIVE and OFFICIAL-SENSTITIVE documentation.
| FR7 | The application must only allow one answer to be selected. |
| FR8 | The application must allow user's to see a hint if they choose. |
| FR9 | The application will not let a user proceed if no answer is selected. |
| FR10| The application must check each answer against the generated solution. |
| FR11| The application must update the user's score when a correct answer is submitted. |
| FR12| The application must store the participant's name, score and timestamp in the quiz_results.csv file upon completion. |
| FR13| The application must allow stored quiz results to be displayed as a leaderboard. |
| FR14| The application must display the final score after all ten questions have been submitted. |
| FR15| The user must be able to restart the quiz as many times as they chose after fully completing each attempt. |

**Non-Functional Requirements**

|  ID  | Requirements |
|------|--------------|
| NFR1 | The application must provide a consistent graphical user interface. |
| NFR2 | The application should run as a standalone Python desktop application. |
| NFR3 | The application must store all the result data in a readable Google Sheets format (.csv file). |
| NFR4 | The font should be clear and readable for all users. |
| NFR5 | The colour scheme should be easy to look at, read and understand. |
| NFR6 | The application must open efficiently when launched and not open behind other windows. |
| NFR7 | The application window must be a fixed size, from the opening page to the questions. |
| NFR8 | The application must be functional offline as well as online. |
| NFR9 | The application must allow the user to select a hint without freezing. |
| NFR10| The application must allow a user to select and submit answer's without freezing or lagging. |
| NFR11| The application must be able to run on Windows desktops and Macbook desktops. |
| NFR12| The application must close efficiently when the 'QUIT' button at the end is clicked. |
| NFR13| The CSV file output must save data cleanly so it opens into Google Sheets correctly. |
| NFR14| The application code must be clearly laid out and simple for updates to not break the main.py file or code. |
| NFR15| The application should be readable using basic software. |

**Technology Stack Outline:**
- [Python 3](https://docs.python.org/3/) — This is the core programming language
- [Tkinter](https://docs.python.org/3/library/tkinter.html) — The desktop graphical user interface (GUI)
- [csv](https://docs.python.org/3/library/csv.html) — Stores local data in CSV format
- [re](https://docs.python.org/3/library/re.html) — Regular Expressions for input validation
- [datetime](https://docs.python.org/3/library/datetime.html) — For timestamp generation

**Code Design Documentation:**
**Figure 2** displays a class design. This is an understandable, structured figure for the key components that make up this quiz application, from the main QuizApp to the smaller components like QuizView and QuizAttempts that make up the full application.

![Figure 2: Class Design (My own design made using Draw.io)](docs_assets/class_design.png)

**Figure 1:** Class Design (My own design made using Draw.io)

## Development
This application is structured across six Python modules, each handling different operations.

load_questions.py loads all the questions from the CSV file:

```
def load_pmo_questions(filename="questions.csv"):
    questions = []
    with open(filename, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            questions.append(row)
    return questions
```
This code ensures the questions have been correctly loaded from the CSV file and can be viewed correctly once the quiz application is run.

quiz_hints.py formats the hints dropdown menu:
```
def create_hint_dropdown(parent, hint_text):
    hint_var = tk.StringVar(value="Need a hint?")
    hints_list = ["Need a hint?", hint_text if hint_text else "No hint available."]
    
    hint_actual = tk.OptionMenu(parent, hint_var, *hints_list)
    hint_actual.config(font=("Century Gothic", 14), fg="#ffffff", bg="#6c114c")
    hint_actual["menu"].config(font=("Century Gothic", 12), fg="#ffffff", bg="#6c114c")
    
    return hint_actual
```

This ensures the text displayed when you open each question is ```Need a hint?``` and returns the actual hint from the CSV file ```return hint_actual```.

quiz_questions.py displays all the questions correctly:

```
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
```
This builds the questions interface while maintaining non-functional requirements like the text colour and readibility of the questions.

This same file also provides the question formatting:
```
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
```

This renders the available multiple-choice options as clickable radio buttons beneath the hint dropdown.

quiz_names.py creates perameters around name entry:
```
def clean_name(name):
    return name.strip().title()

def presence_check(name: str) -> bool:
    return bool(name)

def length_check(name: str) -> bool:
    return 2 <= len(name) <= 35

def character_check(name: str) -> bool:
    return not re.search(r"\d", name)
```
These perameters work together in ```main.py``` to ensure the correct error messages can be displayed once the files are imported.

quiz_attempts.py calculates the number of quiz attempts:
```
    def __init__(self, username):
        self.username = username
        self.score = 0
        self.attempts = 0

    def record_attempt(self, user_answer, expected_answer):
        cleaned_user = str(user_answer).strip().lower()
        cleaned_expected = str(expected_answer).strip().lower()

        print(f"INPUT -> User: '{cleaned_user}' | Expected: '{cleaned_expected}'")
```

This provides the baseline score of ```0```. It then evaluates answers, updates the score, and logs debug information to the terminal:

```
        if cleaned_user == cleaned_expected:
            self.score += 1
            print("-> ✅ Correct! Score increased")
        else:
            print(f"-> ❌ Incorrect (Compared '{cleaned_user}' with '{cleaned_expected}')")
        
        self.attempts += 1
```

The final part of this file is to push the scores and information to the results CSV file and add a timestamp for performance tracking:

```
def save_results(self, filename="quiz_results.csv"):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
```

Finally, main.py brings each element together, including the opening screen and formatting:
```
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
```
The main file also provides all the messages to the user including the final completion score:
```
text=f"Well Done {display_name}!\n\nYou scored: {final_score} / {total_q}"
```
, for example.

## Testing
To ensure the Project Management Quiz App is reliable and user friendly, manual and automated unit testing were essential. This approach covered both the GUI and the coding logic.

**Manual Testing**
Manual testing involved editing each .py file and running them as a regular user would. This included entering valid and invalid names, editing the hint dropdown, checking the ```quiz_results.csv``` file and editing the code.
Justification: These tests ensured the GUI was responsive, the layout was clear and the text and colour's were all rendered correctly. Automated tests do not easily evaluate these elements.

**Automated Testing**
These tests focused on testing individual functions without needing to run ```main.py``` and launching the actual quiz. The name and scoring functions were key elements of these tests.
Justification: Automated testing is quick, identifiable and issues can be easily spotted in the terminal and de-bugged.

**Testing Outcomes:**
**Manual Testing Outcomes**
| Test Case | Test Data | Expected Outcome | Actual Outcome | Pass/Fail |
| Empty Name Test | " " (blank) | Error message: "Name cannot be empty!" | Error message appeared on screen (figure 3) | Pass |
| Short Name Test | "X" | Error message: "Name must be between 2 and 50 characters long!" | Error message appeared on screen | Pass |
| Special Characters Name Test | "B0b!" | Error message: "Name cannot contain numbers or special characters like '!, ?, &'!" | Error message appeared on screen | Pass |
| Valid Name Test | "susan" | Move onto quiz | Name cleaned to "Susan" and moved onto quiz questions | Pass |
| Hint Dropdown | Click the dropdown button | Menu opens showing the relevant hint | Dropdown menu opens showing "Need a hint?" and the correct hint per question | Pass |
| Complete Quiz | Answer all 10 questions | App moves to the final score screen showing the score and "QUIT" button | App moves to the final score screen showing the score and "QUIT" button | Pass |
| CSV file accuracy | Complete quiz and check the CSV file | ```quiz_results.csv``` updates with a new row with the name, score and timestamp | ```quiz_results.csv``` updates with a new row with the name, score and timestamp | Pass |

![Figure 3: Error message displayed successfully](docs_assets/figure3.png)

**Figure 3:** Automated Unit Testing Error (Own coding)

**Automated Testing Outcomes**
While running the Automated Unit Testing tests, the results were not fitering corrrectly to the results CSV file.

As can be seen in Figure 4, ```finish_quiz``` was triggered but no results loaded through to the CSV file.

![Figure 4: Automated Unit Testing Error](docs_assets/figure4.png)

**Figure 4:** Automated Unit Testing Error (Own coding)

To correct this error, each line of code and each .py file had to be troubleshooted and de-bugged. This error was traced to the quiz_attempts.py file where some lines of code were missed:
```
try:
            with open(filename, mode="a", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow([self.username, self.score, timestamp])
            print("-> Results saved successfully to CSV!")
        except Exception as e:
            print(f"-> Error saving results: {e}")
```
This part of the code was essential to saving the information successfully and recording that in the Terminal.

Figure 5 below shows the quiz running successfully and the results and timestamp loaded into the CSV file after a successful test:

![Figure 5: Automated Unit Testing Error](docs_assets/figure5.png)

**Figure 5:** Automated Unit Testing Fix (Own coding)

Eventually, all manual and automated tests were passed successfully!

## Documentation
**User Documentation**
Welcome to the Project Management Office Quiz Application. This guide outlines how users and staff members can use this quiz during the onboarding process.

1. Launch the application through ```main.py``` file.
2. An opening screen will launch, welcoming you to the quiz. On this page, you will be prompted to enter your name. This must be between 2-35 characters and contain no numbers or special characters.
3. Once the name is entered correctly, click "Start Quiz" to begin.
4. You will be presented with 10 multiple choice questions, one after the other, focusing on basic Project Management scenarios. These include governance, administration and sensitive data handling.
5. For each question, read the question, select a dropdown hint if needed and select your preferred answer using the buttons on the left.
6. After submitting your answers for all 10 questions, the application wil automatically calculate your total score, displaying at the same time as your personalised congratulatory completion message.
7. When finished, click the "QUIT" button to exit and close the program.

**Testing Documentation**
This application was built in Python using the ```tkinter``` GUI framework. The application follows a modular structure across three python scripts.
    - load_questions.py
    - quiz_hints.py
    - quiz_names.py
    - quiz_questions.py
    - quiz_attempts.py
    - main.py
```load_questions.py``` pulls the questions from the CSV file (```questions.csv```) while
```main.py``` acts as the central component, pulling each framework together and triggering the results to format into a table, ```quiz_results.csv```.

To run automated tests locally, testers and developers can execute scripts directly via the terminal without needing to launch the full GUI. The automatic filtering of names, times and scores into the CSV file allows hiring staff to easily analyse onboarding statistics and results into Google Sheets or equivalent spreadsheets.

## Evaluation
Developing this application has been great to understand ```tkinter```, basic software development and how I can practically apply each element to my specific job role, in the Project Management office. Below is a summary of what went well and even better if, to highlight current success but also spot growth opportunities.

**What Went Well:**
    - Modular Architecture: Splitting the code across multiple Python and CSV files makes the code much easier to edit, troubleshoot, de-bug and interpret. This is useful for testers and developers as the code is more organised and well-defined.
    - Structured Data Storage: Resolving the results CSV file error was a big milestone. The application now reliably pushes names, timestamps and scores into this easy-to-understand file which can be extracted to Google Sheets or equivalent.
    - Hint Dropdowns: The hints button works as intended which was an important element of the quiz. It adds an extra dimension to make the experience better for quiz-takers. 
    - User Interface: The GUI is clear to understand, where mistakes are inputted, clear guidance is presented to the user and any error's can be overcome efficiently.

**Even Better If...**
    - Feedback: The application would be better if feedback was provided per incorrect question answered, like a pop-up before moving on to the next question.
    - Results Analysis: The CSV file only records the basic information, which is easy to understand, but it could be developed through the addition of trend analysis.
    - Past Performance Dashboard: Where an interface could recognise a user that has taken the test before and remind them of their previous scores before they re-take the test. This would help understand if and where improvements are being made over the application.

In conclusion, this quiz is a useful tool to assess whether employees are ready for the practicalities of the Project Management office over more technical or developmental roles. This tool effectively supports hiring staff while providing a clear and easy experience for users. It provides a good foundational assessment with lots of room for improvement in the future.